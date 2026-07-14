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

for model in client.models.list():
    print(model.name)


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

    try:

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=full_prompt
        )

        response_text = response.text.strip()

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

        analysis = json.loads(response_text)

        return analysis

    except Exception as e:

        print("\nERROR FROM GEMINI\n")
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

            "summary": "The AI service is temporarily unavailable. Please try again later.",

            "strengths": [],

            "weaknesses": [],

            "missing_skills": [],

            "missing_keywords": [],

            "suggestions": [],

            "recommended_roles": [],

            "interview_questions": []

        }