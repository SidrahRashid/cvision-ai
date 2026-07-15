from flask import (
    Flask,
    render_template,
    request,
    session,
    send_file
)
from io import BytesIO
from utils.report_generator import generate_pdf
from utils.pdf_reader import read_pdf
from utils.gemini import analyze_resume

app = Flask(__name__)
app.secret_key = "cvision-secret-key"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    # No file uploaded
    if "resume" not in request.files:
        return render_template(
            "result.html",
            analysis={
                "ats_score": 0,
                "section_scores": {
                    "technical_skills": 0,
                    "projects": 0,
                    "experience": 0,
                    "education": 0,
                    "formatting": 0,
                    "keyword_optimization": 0
                },
                "summary": "No resume was uploaded.",
                "strengths": [],
                "weaknesses": [],
                "missing_skills": [],
                "missing_keywords": [],
                "suggestions": [],
                "recommended_roles": [],
                "interview_questions": []
            }
        )

    resume = request.files["resume"]

    # Empty filename
    if resume.filename == "":
        return render_template(
            "result.html",
            analysis={
                "ats_score": 0,
                "section_scores": {
                    "technical_skills": 0,
                    "projects": 0,
                    "experience": 0,
                    "education": 0,
                    "formatting": 0,
                    "keyword_optimization": 0
                },
                "summary": "Please select a PDF resume.",
                "strengths": [],
                "weaknesses": [],
                "missing_skills": [],
                "missing_keywords": [],
                "suggestions": [],
                "recommended_roles": [],
                "interview_questions": []
            }
        )

    # Only PDF files
    if not resume.filename.lower().endswith(".pdf"):
        return render_template(
            "result.html",
            analysis={
                "ats_score": 0,
                "section_scores": {
                    "technical_skills": 0,
                    "projects": 0,
                    "experience": 0,
                    "education": 0,
                    "formatting": 0,
                    "keyword_optimization": 0
                },
                "summary": "Only PDF resumes are supported.",
                "strengths": [],
                "weaknesses": [],
                "missing_skills": [],
                "missing_keywords": [],
                "suggestions": [],
                "recommended_roles": [],
                "interview_questions": []
            }
        )

    # Read PDF
    print("PDF extracted")
    resume_text = read_pdf(resume)
    print("Calling Gemini...")
    analysis = analyze_resume(resume_text)
    session["analysis"] = analysis
    print("Gemini finished")

    if not resume_text.strip():
        return render_template(
            "result.html",
            analysis={
                "ats_score": 0,
                "section_scores": {
                    "technical_skills": 0,
                    "projects": 0,
                    "experience": 0,
                    "education": 0,
                    "formatting": 0,
                    "keyword_optimization": 0
                },
                "summary": "Unable to extract text from the uploaded PDF.",
                "strengths": [],
                "weaknesses": [],
                "missing_skills": [],
                "missing_keywords": [],
                "suggestions": [],
                "recommended_roles": [],
                "interview_questions": []
            }
        )

    # AI Analysis
    analysis = analyze_resume(resume_text)

    print("\n========== FINAL ANALYSIS ==========\n")
    print(analysis)
    print("\n====================================\n")

    return render_template(
        "result.html",
        analysis=analysis
    )

@app.route("/download-report")
def download_report():

    analysis = session.get("analysis")

    if not analysis:
        return "No report available.", 404

    pdf = generate_pdf(analysis)

    return send_file(

        BytesIO(pdf),

        as_attachment=True,

        download_name="CVision_Report.pdf",

        mimetype="application/pdf"

    )

if __name__ == "__main__":
    app.run(debug=True, threaded=True)