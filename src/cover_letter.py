"""
ApplyMate AI - Cover Letter Generator
=======================================
Uses Groq (default) or Gemini (user key).
"""

import streamlit as st
import json
import re
import sys
import os
sys.path.append(os.path.dirname(__file__))
from ai_helper import ask_groq, ask_gemini


def generate_cover_letter(resume_text: str, jd_text: str, user_name: str = "", company_name: str = "", role_name: str = "", ai_mode: str = "groq", user_key: str = None) -> dict:
    prompt = f"""
You are an expert career coach and professional cover letter writer.
Generate a tailored cover letter based on:

CANDIDATE NAME: {user_name if user_name else "the candidate"}
COMPANY NAME: {company_name if company_name else "the company"}
ROLE: {role_name if role_name else "the position"}

JOB DESCRIPTION:
{jd_text[:2500]}

RESUME:
{resume_text[:2500]}

Instructions:
- Write a compelling 3-4 paragraph cover letter
- Match keywords from the JD naturally
- Highlight the most relevant projects and skills with metrics
- Keep it under 400 words, professional but not robotic

Return ONLY a valid JSON object (no markdown, no extra text):
{{
    "subject_line": "Application for Machine Learning Engineer",
    "cover_letter": "Dear Hiring Manager,\\n\\n[paragraph 1]\\n\\n[paragraph 2]\\n\\n[paragraph 3]\\n\\nSincerely,\\n{user_name if user_name else 'Your Name'}",
    "key_points_used": ["point1", "point2", "point3"],
    "tips": ["tip1", "tip2"]
}}
"""
    if ai_mode == "gemini" and user_key:
        raw = ask_gemini(prompt, user_key, max_tokens=2500)
    else:
        raw = ask_groq(prompt, max_tokens=2500)

    if not raw:
        return None
    try:
        raw = re.sub(r'```json\s*', '', raw)
        raw = re.sub(r'```\s*', '', raw)
        return json.loads(raw.strip())
    except:
        try:
            json_match = re.search(r'\{.*\}', raw, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass
        return None
