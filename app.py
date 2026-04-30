from flask import Flask, render_template, request
from openai import OpenAI
import os
import re

app = Flask(__name__)

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# ================= MAIN HOME =================
@app.route("/")
def home():
    return render_template("index.html")


# ================= AI CONTENT GENERATOR =================
@app.route("/ai-content-generator", methods=["GET", "POST"])
def ai_content():
    response_text = ""

    if request.method == "POST":
        user_input = request.form.get("prompt")

        prompt = f"Write a fully SEO optimized article about {user_input}"

        try:
            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[{"role": "user", "content": prompt}]
            )

            response_text = clean(response.choices[0].message.content)

        except Exception as e:
            response_text = str(e)

    return render_template("tool.html", response=response_text, title="AI Content Generator")


# ================= HUMANIZER =================
@app.route("/humanize-ai-text", methods=["GET", "POST"])
def humanize():
    response_text = ""

    if request.method == "POST":
        user_input = request.form.get("prompt")

        prompt = f"Rewrite this content in a natural human tone:\n{user_input}"

        try:
            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[{"role": "user", "content": prompt}]
            )

            response_text = clean(response.choices[0].message.content)

        except Exception as e:
            response_text = str(e)

    return render_template("tool.html", response=response_text, title="Humanize AI Text")


# ================= AI DETECTOR =================
@app.route("/ai-detector-free", methods=["GET", "POST"])
def detector():
    response_text = ""

    if request.method == "POST":
        user_input = request.form.get("prompt")

        prompt = f"Analyze if this content is AI or human. Give percentage:\n{user_input}"

        try:
            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[{"role": "user", "content": prompt}]
            )

            response_text = clean(response.choices[0].message.content)

        except Exception as e:
            response_text = str(e)

    return render_template("tool.html", response=response_text, title="AI Detector")


# ================= SEO WRITER =================
@app.route("/free-seo-writer", methods=["GET", "POST"])
def seo_writer():
    response_text = ""

    if request.method == "POST":
        user_input = request.form.get("prompt")

        prompt = f"Write SEO optimized content about {user_input}"

        try:
            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[{"role": "user", "content": prompt}]
            )

            response_text = clean(response.choices[0].message.content)

        except Exception as e:
            response_text = str(e)

    return render_template("tool.html", response=response_text, title="SEO Writer")


# ================= PARAGRAPH =================
@app.route("/ai-paragraph-generator", methods=["GET", "POST"])
def paragraph():
    response_text = ""

    if request.method == "POST":
        user_input = request.form.get("prompt")

        prompt = f"Write a high-quality paragraph about {user_input}"

        try:
            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[{"role": "user", "content": prompt}]
            )

            response_text = clean(response.choices[0].message.content)

        except Exception as e:
            response_text = str(e)

    return render_template("tool.html", response=response_text, title="Paragraph Generator")


# ================= CLEAN FUNCTION =================
def clean(text):
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    text = re.sub(r"[#*_`>-]", "", text)
    text = text.replace("---", "")
    text = re.sub(r"\n\s*\n", "\n\n", text)
    return text.strip()
    
with app.app_context():
    db.create_all()

# ================= RUN =================
if __name__ == "__main__":
    app.run(debug=True)
