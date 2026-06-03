"""
ApplyMate AI - Cover Letter Generator
=======================================
Uses Google Gemini API to generate tailored, professional cover letters.
"""

import google.generativeai as genai
import streamlit as st
import re


def configure_gemini():
    """Configure Gemini API with key from Streamlit secrets."""
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
        genai.configure(api_key=api_key)
        return genai.GenerativeModel("gemini-2.0-flash")
    except Exception as e:
        st.error("⚠️ Gemini API key not found. Please add it in Streamlit secrets.")
        return None


def generate_cover_letter(resume_text: str, jd_text: str, user_name: str = "", company_name: str = "", role_name: str = "") -> dict:
    """
    Generate a tailored cover letter using Gemini AI.
    Returns dict with cover_letter, subject_line, and tips.
    """
    model = configure_gemini()
    if not model:
        return None

    prompt = f"""
You are an expert career coach and professional cover letter writer.

Generate a tailored, professional cover letter based on the following:

CANDIDATE NAME: {user_name if user_name else "the candidate"}
COMPANY NAME: {company_name if company_name else "the company"}
ROLE: {role_name if role_name else "the position"}

JOB DESCRIPTION:
{jd_text[:2500]}

CANDIDATE'S RESUME:
{resume_text[:2500]}

Instructions:
- Write a compelling 3-4 paragraph cover letter
- Match keywords from the JD naturally
- Highlight the candidate's most relevant projects and skills
- Show genuine enthusiasm for the role
- Keep it under 400 words
- Professional but not robotic tone
- Include specific achievements from the resume with numbers/metrics where possible

Return ONLY a valid JSON object (no markdown, no extra text):
{{
    "subject_line": "Application for Machine Learning Engineer — Dnyaneshwar Gumalwad",
    "cover_letter": "Dear Hiring Manager,\\n\\n[paragraph 1]\\n\\n[paragraph 2]\\n\\n[paragraph 3]\\n\\nSincerely,\\n{user_name if user_name else 'Your Name'}",
    "key_points_used": ["point1", "point2", "point3"],
    "tips": ["tip1", "tip2"]
}}
"""

    try:
        response = model.generate_content(prompt)
        raw = response.text.strip()

        # Clean markdown if present
        raw = re.sub(r'```json\s*', '', raw)
        raw = re.sub(r'```\s*', '', raw)
        raw = raw.strip()

        import json
        result = json.loads(raw)
        return result

    except Exception as e:
        st.error(f"Cover letter generation failed: {str(e)}")
        return None
