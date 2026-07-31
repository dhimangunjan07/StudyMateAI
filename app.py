from flask import Flask, render_template, request
from dotenv import load_dotenv
from groq import Groq
import markdown
import os

# ---------------- LOAD ENV ---------------- #

load_dotenv()

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
You are StudyMateAI.

Rules:

1. Explain everything in simple language.

2. Solve mathematics step by step.

3. If the question is programming:
   - Give the code inside Markdown code blocks.
   - Explain the code using bullet points.
   - Show the expected output inside a text code block.

4. If theory:
   - Use headings.
   - Use bullet points.
   - Give examples.

5. If comparison:
   - Use Markdown tables.

6. Never return code in paragraph format.

7. Always format answers using proper Markdown.
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

            raw_answer = response.choices[0].message.content

            answer = markdown.markdown(
                raw_answer,
                extensions=[
                    "fenced_code",
                    "tables"
                ]
            )

        except Exception as e:

            answer = f"<b>Error:</b> {e}"

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