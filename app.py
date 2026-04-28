from flask import Flask, render_template, request
from openai import OpenAI
import os
import re

app = Flask(__name__)

# 🔐 API KEY from environment (Render)
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@app.route("/", methods=["GET", "POST"])
def index():
    response_text = ""

    if request.method == "POST":
        user_input = request.form.get("prompt")
        mode = request.form.get("mode")

        # 🔥 MODE LOGIC
        if mode == "seo":
            prompt = f"Write a clean, human-like SEO article about {user_input}. Include title, meta description, and headings. Do not use markdown symbols."

        elif mode == "humanize":
            prompt = f"Rewrite this content in a natural, human-like tone:\n{user_input}"

        elif mode == "detect":
            prompt = f"Analyze this content and tell if it is AI or human-written. Give percentage and explanation:\n{user_input}"

        elif mode == "count":
            prompt = f"Count total words, sentences, and characters in this text:\n{user_input}"

        elif mode == "image":
            prompt = f"Create a detailed AI image prompt based on this idea:\n{user_input}"

        else:
            prompt = user_input

        try:
            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            response_text = response.choices[0].message.content

            # 🔥 CLEAN OUTPUT (remove markdown junk)
            response_text = re.sub(r"[#*`]", "", response_text)
            response_text = response_text.replace("---", "")

        except Exception as e:
            response_text = f"Error: {str(e)}"

    return render_template("index.html", response=response_text)


if __name__ == "__main__":
    app.run(debug=True)
