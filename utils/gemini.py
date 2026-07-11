import os
import json
from datetime import datetime

import google.generativeai as genai
from dotenv import load_dotenv

from utils.prompts import PROMPT

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def analyze_resume(resume_text):

    # Get current month and year
    current_date = datetime.now().strftime("%B %Y")

    # Build prompt
    full_prompt = f"""
Today's date is {current_date}.

When evaluating the resume:
- Treat today's date as the reference date.
- Do NOT mark work experience before today's date as a future date.
- Do NOT incorrectly flag valid employment dates.
- Evaluate the resume based on the current date.

{PROMPT}

Resume:

{resume_text}
"""

    model = genai.GenerativeModel("gemini-2.5-flash")

    response = model.generate_content(full_prompt)

    response_text = response.text.strip()

    print("\n========== GEMINI RESPONSE ==========\n")
    print(response_text)
    print("\n=====================================\n")

    # Remove Markdown code fences if Gemini returns them
    if response_text.startswith("```json"):
        response_text = response_text.replace("```json", "", 1)

    if response_text.startswith("```"):
        response_text = response_text.replace("```", "", 1)

    if response_text.endswith("```"):
        response_text = response_text[:-3]

    response_text = response_text.strip()

    try:

        analysis = json.loads(response_text)

        return analysis

    except json.JSONDecodeError as e:

        print("\nJSON PARSE ERROR")
        print(e)
        print("\nRAW RESPONSE:\n")
        print(response_text)

        return {
            "ats_score": 0,
            "section_scores": {
                "technical_skills": 0,
                "projects": 0,
                "experience": 0,
                "education": 0,
                "formatting": 0,
                "keyword_optimization": 0
            },
            "summary": "The AI returned an invalid response. Please try again.",
            "strengths": [],
            "weaknesses": [],
            "missing_skills": [],
            "missing_keywords": [],
            "suggestions": [],
            "recommended_roles": [],
            "interview_questions": []
        }

    except Exception as e:

        print("\nUNEXPECTED ERROR")
        print(e)

        return {
            "ats_score": 0,
            "section_scores": {
                "technical_skills": 0,
                "projects": 0,
                "experience": 0,
                "education": 0,
                "formatting": 0,
                "keyword_optimization": 0
            },
            "summary": "Something went wrong while analyzing the resume.",
            "strengths": [],
            "weaknesses": [],
            "missing_skills": [],
            "missing_keywords": [],
            "suggestions": [],
            "recommended_roles": [],
            "interview_questions": []
        }