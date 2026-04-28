from flask import Flask, render_template, request
from openai import OpenAI
import os

app = Flask(__name__)

# 🔐 API KEY (from Render environment variable)
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@app.route("/", methods=["GET", "POST"])
def index():
    response_text = ""

    if request.method == "POST":
        user_input = request.form.get("prompt")
        mode = request.form.get("mode")

        # 🧠 MODE LOGIC
        if mode == "seo":
            prompt = f"Write a fully SEO optimized article about: {user_input}. Include headings, keywords, and meta description."

        elif mode == "humanize":
            prompt = f"Rewrite this content in a natural, human-like way:\n\n{user_input}"

        elif mode == "detect":
            prompt = f"Analyze this content and tell if it is AI-generated or human-written. Give percentage and explanation:\n\n{user_input}"

        elif mode == "count":
            prompt = f"Count total words, sentences, and characters in this text:\n\n{user_input}"

        elif mode == "image":
            prompt = f"Create a detailed AI image prompt for this idea:\n\n{user_input}"

        else:
            prompt = user_input

        try:
            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful AI tool."},
                    {"role": "user", "content": prompt}
                ]
            )

            response_text = response.choices[0].message.content

        except Exception as e:
            response_text = f"Error: {str(e)}"

    return render_template("index.html", response=response_text)


if __name__ == "__main__":
    app.run(debug=True)
