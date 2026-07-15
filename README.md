# 🚀 CVision

### AI-Powered Resume Analyzer

CVision is an intelligent resume analysis platform that evaluates resumes using Google's Gemini AI. It provides an ATS score, identifies strengths and weaknesses, suggests improvements, recommends career roles, generates interview questions, and allows users to download a professional PDF report—all within seconds.

---

## ✨ Features

- 📄 Upload resumes in PDF format
- 🤖 AI-powered resume analysis using Google Gemini
- 📊 ATS Score (0–100)
- 📈 Section-wise score breakdown
- 💪 Resume strengths detection
- ⚠️ Weakness identification
- 🧠 Missing skills analysis
- 💼 Career role recommendations
- 🎤 AI-generated interview questions
- 💡 Personalized improvement suggestions
- 📑 Downloadable PDF report
- 🎯 Resume vs Job Description matching (optional)
- 📱 Responsive modern UI

---

## 🖼️ Screenshots

### Home Page

> Add screenshot here

![Homepage](screenshots/homepage.png)

---

### Resume Analysis

> Add screenshot here

![Analysis](screenshots/analysis.png)

---

### PDF Report

> Add screenshot here

![PDF Report](screenshots/pdf-report.png)

---

## 🛠️ Tech Stack

### Backend

- Python
- Flask

### Artificial Intelligence

- Google Gemini API

### Frontend

- HTML5
- Tailwind CSS
- JavaScript

### PDF Processing

- PyMuPDF
- ReportLab

---

## 📂 Project Structure

```
CVision/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   ├── favicon.svg
│   ├── images/
│   └── icons/
│
├── utils/
│   ├── gemini.py
│   ├── pdf_reader.py
│   ├── prompts.py
│   └── report_generator.py
│
└── screenshots/
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/CVision.git
```

Move into the project

```bash
cd CVision
```

Create a virtual environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

## ▶️ Running the Project

Start the Flask server

```bash
python app.py
```

Visit

```
http://127.0.0.1:5000
```

---

## 📋 How It Works

1. Upload a resume in PDF format.
2. (Optional) Paste a Job Description.
3. CVision extracts text using PyMuPDF.
4. Google Gemini analyzes the resume.
5. ATS score and detailed insights are generated.
6. Users can download a professional PDF report.

---

## 🎯 Future Improvements

- Multi-page resume comparison
- Resume templates
- Cover letter generation
- AI resume rewriting
- Authentication system
- Resume history
- Dashboard analytics
- Multiple language support

---

## 📈 Version

**CVision v1.0.0**

---

## 🌐 Live Demo

> Add your deployed Render URL here

```
https://cvision-ai-1.onrender.com```

---

## 💻 GitHub Repository

https://github.com/SidrahRashid/cvision-ai
```
```

---

## 👩‍💻 Author

**Sidrah Rashid**

B.Sc. Data Science Student

Kolkata, India

LinkedIn: https://www.linkedin.com/in/sidrah-rashid/
GitHub: https://github.com/SidrahRashid

---

## 📄 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub. It helps others discover the project and supports my work.

---

Made with ❤️ using Flask, Google Gemini AI, Tailwind CSS and PyMuPDF.