"""
ApplyMate AI - Skill Gap Roadmap Generator
==========================================
Uses Groq (default) or Gemini (user key).
"""

import json
import re
import sys
import os
sys.path.append(os.path.dirname(__file__))
from ai_helper import ask_groq, ask_gemini


def generate_skill_roadmap(resume_text: str, jd_text: str, ai_mode: str = "groq", user_key: str = None) -> dict:
    prompt = f"""
You are an expert career coach and technical mentor.
Create a personalized skill gap roadmap.

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
        {{"skill": "Python", "level": "Advanced", "relevance": "Critical"}}
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
            "how_to_add_to_resume": "Containerize your existing ML projects"
        }}
    ],
    "week_by_week_plan": [
        {{"week": 1, "focus": "Docker basics + containerize one project", "goal": "Have Docker on resume"}},
        {{"week": 2, "focus": "FastAPI — build ML model API", "goal": "Deploy model as REST API"}},
        {{"week": 3, "focus": "Practice interview questions", "goal": "Interview ready"}}
    ],
    "overall_tip": "You are 72% ready for this role. Focus on Docker and API deployment."
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
