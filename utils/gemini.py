import os
import json
from datetime import datetime

from google import genai
from dotenv import load_dotenv

from utils.prompts import PROMPT

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def analyze_resume(resume_text):

    current_date = datetime.now().strftime("%B %Y")

    full_prompt = f"""
Today's date is {current_date}.

When evaluating the resume:

- Treat today's date as the reference.
- Never mark previous employment as future experience.
- Do not invent weaknesses.
- Only identify genuine issues.
- Return ONLY valid JSON.
- Do not wrap the JSON inside markdown.

{PROMPT}

Resume:

{resume_text}
"""

    models = [
        "gemini-flash-latest",
        "gemini-3.1-flash-lite",
        "gemini-2.0-flash-lite",
    ]

    response_text = None
    last_error = None

    for model_name in models:

        try:

            print(f"\nTrying model: {model_name}")

            response = client.models.generate_content(
                model=model_name,
                contents=full_prompt
            )

            response_text = response.text.strip()

            print(f"Success with {model_name}")

            break

        except Exception as e:

            print(f"{model_name} failed:")
            print(e)

            last_error = e

    if response_text is None:

        print("\n========== ALL MODELS FAILED ==========")
        print(last_error)
        print("=======================================\n")

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

            "summary": "Google Gemini is currently unavailable. Please try again in a minute.",

            "strengths": [],
            "weaknesses": [],
            "missing_skills": [],
            "missing_keywords": [],
            "suggestions": [],
            "recommended_roles": [],
            "interview_questions": []

        }

    print("\n========== GEMINI RESPONSE ==========\n")
    print(response_text)
    print("\n=====================================\n")

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

    except Exception:

        print("\nInvalid JSON returned by Gemini\n")

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