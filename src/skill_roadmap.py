"""
ApplyMate AI - Skill Gap Roadmap Generator
==========================================
Uses Google Gemini API to generate personalized skill roadmaps.
"""

import google.generativeai as genai
import streamlit as st
import json
import re


def configure_gemini():
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
        genai.configure(api_key=api_key)
        return genai.GenerativeModel("gemini-2.0-flash")
    except Exception as e:
        st.error("⚠️ Gemini API key not found.")
        return None


def generate_skill_roadmap(resume_text: str, jd_text: str) -> dict:
    """Generate a personalized skill gap roadmap using Gemini AI."""
    model = configure_gemini()
    if not model:
        return None

    prompt = f"""
You are an expert career coach and technical mentor.

Analyze the resume and job description below, then create a personalized skill gap roadmap.

JOB DESCRIPTION:
{jd_text[:2500]}

RESUME:
{resume_text[:2500]}

Return ONLY a valid JSON object (no markdown, no extra text):
{{
    "current_level": "Junior ML Engineer",
    "target_level": "ML Engineer at GlobalLogic",
    "readiness_score": 72,
    "skills_you_have": [
        {{"skill": "Python", "level": "Advanced", "relevance": "Critical"}},
        {{"skill": "Machine Learning", "level": "Intermediate", "relevance": "Critical"}}
    ],
    "skills_to_learn": [
        {{
            "skill": "Docker",
            "priority": "High",
            "time_to_learn": "2 weeks",
            "free_resources": [
                {{"name": "Docker Official Tutorial", "url": "https://docs.docker.com/get-started/"}},
                {{"name": "Docker for Beginners - YouTube", "url": "https://www.youtube.com/watch?v=fqMOX6JJhGo"}}
            ],
            "how_to_add_to_resume": "Add a Docker project — containerize your existing ML projects"
        }},
        {{
            "skill": "FastAPI",
            "priority": "Medium",
            "time_to_learn": "1 week",
            "free_resources": [
                {{"name": "FastAPI Official Docs", "url": "https://fastapi.tiangolo.com/tutorial/"}},
                {{"name": "FastAPI Course - YouTube", "url": "https://www.youtube.com/watch?v=0sOvCWFmrtA"}}
            ],
            "how_to_add_to_resume": "Build a REST API for your Credit Card Fraud Detection model"
        }}
    ],
    "week_by_week_plan": [
        {{"week": 1, "focus": "Docker basics + containerize one project", "goal": "Have Docker on resume"}},
        {{"week": 2, "focus": "FastAPI — build ML model API", "goal": "Deploy model as REST API"}},
        {{"week": 3, "focus": "Practice interview questions + polish GitHub", "goal": "Interview ready"}}
    ],
    "overall_tip": "You are 72% ready for this role. Focus on Docker and API deployment to close the gap quickly."
}}

Priority must be: High, Medium, or Low
Level must be: Beginner, Intermediate, or Advanced
Relevance must be: Critical, Important, or Optional
"""

    try:
        response = model.generate_content(prompt)
        raw = response.text.strip()
        raw = re.sub(r'```json\s*', '', raw)
        raw = re.sub(r'```\s*', '', raw)
        raw = raw.strip()
        result = json.loads(raw)
        return result
    except Exception as e:
        st.error(f"Roadmap generation failed: {str(e)}")
        return None
