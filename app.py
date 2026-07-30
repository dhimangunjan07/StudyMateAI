from flask import Flask, render_template, request
from dotenv import load_dotenv
from groq import Groq
import os

# Load .env
load_dotenv()

# Groq Client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

app = Flask(__name__)

# ---------------- HOME ---------------- #

@app.route("/")
def home():
    return render_template("index.html")


# ---------------- ABOUT ---------------- #

@app.route("/about")
def about():
    return render_template("about.html")


# ---------------- CHAT ---------------- #

@app.route("/chat", methods=["GET", "POST"])
def chat():

    question = ""
    answer = ""

    if request.method == "POST":

        question = request.form["question"]

        try:

            response = client.chat.completions.create(

                model="llama-3.3-70b-versatile",

                messages=[

                    {
                        "role": "system",
                        "content": """
You are HomeworkAI.

Rules:

1. Explain every answer simply.

2. Solve mathematics step-by-step.

3. If coding question:
   - Give code.
   - Explain code.

4. If theory:
   - Explain with examples.

5. Always be student friendly.
"""
                    },

                    {
                        "role": "user",
                        "content": question
                    }

                ],

                temperature=0.5,

                max_tokens=1024

            )

            answer = response.choices[0].message.content

        except Exception as e:

            answer = str(e)

    return render_template(

        "chat.html",

        question=question,

        answer=answer

    )


# ---------------- UPLOAD ---------------- #

@app.route("/upload", methods=["GET", "POST"])
def upload():

    filename = ""

    if request.method == "POST":

        file = request.files["file"]

        if file:

            filename = file.filename

    return render_template(

        "upload.html",

        filename=filename

    )


# ---------------- RUN ---------------- #

if __name__ == "__main__":
    app.run(debug=True)