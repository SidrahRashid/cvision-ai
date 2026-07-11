from flask import Flask, render_template, request
from utils.pdf_reader import read_pdf
from utils.gemini import analyze_resume

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    if "resume" not in request.files:
        return "No file uploaded."

    resume = request.files["resume"]

    if resume.filename == "":
        return "Please select a PDF file."

    if not resume.filename.lower().endswith(".pdf"):
        return "Only PDF files are allowed."

    # Extract text from PDF
    resume_text = read_pdf(resume)

    # Analyze with Gemini
    analysis = analyze_resume(resume_text)

    # Debug (optional)
    print("\n========== FINAL ANALYSIS ==========\n")
    print(analysis)
    print("\n====================================\n")

    return render_template(
        "result.html",
        analysis=analysis
    )


if __name__ == "__main__":
    app.run(debug=True)