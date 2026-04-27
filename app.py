from flask import Flask, request, render_template
from openai import OpenAI

app = Flask(__name__)

# 🔑 ADD YOUR API KEY HERE
client = OpenAI(api_key="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")


@app.route("/", methods=["GET", "POST"])
def index():
    response_text = ""

    if request.method == "POST":
        mode = request.form["mode"]
        user_input = request.form["prompt"]

        # 🔥 WORD COUNT (no API needed)
        if mode == "count":
            word_count = len(user_input.split())
            response_text = f"Word Count: {word_count}"

        else:
            # 🔥 DEFINE PROMPTS
            if mode == "seo":
                system_prompt = """You are an SEO expert.

Generate:
- SEO Title
- Meta Description
- Keywords
- Outline
- Full Article

Use clean formatting. No symbols like ## or **.
"""

            elif mode == "humanize":
                system_prompt = """Rewrite the text in a natural human tone.
Make it engaging, simple, and remove AI patterns.
"""

            elif mode == "detect":
                system_prompt = """Analyze the text and estimate if it is AI-generated or human-written.
Give percentage and explanation.
"""

            elif mode == "image":
                system_prompt = """Create a detailed image generation prompt based on the text.
"""

            # 🔥 CALL AI
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ]
            )

            response_text = response.choices[0].message.content

    return render_template("index.html", response=response_text)


if __name__ == "__main__":
    app.run(debug=True)