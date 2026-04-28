from flask import Flask, request, render_template
from openai import OpenAI
import os

app = Flask(__name__)

# API key from environment
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@app.route("/", methods=["GET", "POST"])
def index():
    try:
        response_text = ""

        if request.method == "POST":
            mode = request.form.get("mode")
            user_input = request.form.get("prompt")

            if mode == "count":
                word_count = len(user_input.split())
                response_text = f"Word Count: {word_count}"

            else:
                system_prompt = "You are a helpful assistant."

                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_input}
                    ]
                )

                response_text = response.choices[0].message.content

        return render_template("index.html", response=response_text)

    except Exception as e:
        return f"ERROR: {str(e)}"  # 🔥 will show real issue

if __name__ == "__main__":
    app.run()