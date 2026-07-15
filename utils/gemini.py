import os
import json
import re
from datetime import datetime

from dotenv import load_dotenv
from google import genai

from utils.prompts import PROMPT

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


DEFAULT_RESPONSE = {
    "ats_score": 0,
    "section_scores": {
        "technical_skills": 0,
        "projects": 0,
        "experience": 0,
        "education": 0,
        "formatting": 0,
        "keyword_optimization": 0
    },
    "summary": "",
    "strengths": [],
    "weaknesses": [],
    "missing_skills": [],
    "missing_keywords": [],
    "suggestions": [],
    "recommended_roles": [],
    "interview_questions": []
}


def clean_json(text: str):

    text = text.strip()

    text = re.sub(r"^```json", "", text, flags=re.IGNORECASE)
    text = re.sub(r"^```", "", text)
    text = re.sub(r"```$", "", text)

    return text.strip()


def analyze_resume(resume_text):

    current_date = datetime.now().strftime("%B %Y")

    prompt = f"""
Today's date is {current_date}.

Rules:

- Use today's date as reference.
- Never assume information.
- Never invent weaknesses.
- Return ONLY valid JSON.

{PROMPT}

{resume_text}
"""

    # Most stable first
    models = [
        "gemini-3.1-flash-lite",
        "gemini-flash-latest"
    ]

    last_error = None

    for model in models:

        try:

            print(f"\nTrying {model}")

            response = client.models.generate_content(
                model=model,
                contents=prompt
            )

            text = clean_json(response.text)

            analysis = json.loads(text)

            print(f"Success using {model}")

            return analysis

        except Exception as e:

            print(f"{model} failed")

            print(e)

            last_error = e

            continue

    print("\nAll Gemini models failed\n")

    print(last_error)

    result = DEFAULT_RESPONSE.copy()

    result["summary"] = (
        "The AI service is temporarily unavailable. "
        "Please try again in a few moments."
    )

    return result