from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

# API KEY
openai.api_key = os.environ.get("OPENAI_API_KEY")


# ================= HOME =================
@app.route("/")
def home():
    return render_template("index.html")


# ================= CHAT API =================
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )

        reply = response["choices"][0]["message"]["content"]

    except Exception as e:
        reply = "Error: " + str(e)

    return jsonify({"reply": reply})


# ================= RUN =================
if __name__ == "__main__":
    app.run()
