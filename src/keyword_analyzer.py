"""
ApplyMate AI - AI Keyword Gap Analyzer
========================================
Uses Groq (default) or Gemini (user key) for keyword analysis.
"""

import streamlit as st
import json
import re
import sys
import os
sys.path.append(os.path.dirname(__file__))
from ai_helper import ask_groq, ask_gemini


def analyze_keywords_with_ai(resume_text: str, jd_text: str, ai_mode: str = "groq", user_key: str = None) -> dict:
    prompt = f"""
You are an expert ATS analyst and career coach.
Analyze the Job Description and Resume below.

JOB DESCRIPTION:
{jd_text[:3000]}

RESUME:
{resume_text[:3000]}

Return ONLY a valid JSON object (no markdown, no extra text):
{{
    "found_keywords": [
        {{"keyword": "python", "category": "Programming", "importance": "Critical"}}
    ],
    "missing_keywords": [
        {{"keyword": "docker", "category": "DevOps", "importance": "Important", "suggestion": "Add Docker experience in your projects section"}}
    ],
    "match_percentage": 72,
    "summary": "Your resume is a strong match. Focus on adding Docker and REST API keywords.",
    "top_3_priorities": ["Add Docker to skills", "Mention REST API experience", "Add communication examples"]
}}
Categories: Programming, AI/ML, Data Science, DevOps/Cloud, Web/API, Soft Skills, Domain Knowledge, Tools
Importance: Critical, Important, Optional
"""
    if ai_mode == "gemini" and user_key:
        raw = ask_gemini(prompt, user_key)
    else:
        raw = ask_groq(prompt)

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


def get_importance_color(importance: str) -> tuple:
    if importance == "Critical":
        return ("rgba(255, 99, 99, 0.15)", "#FF6363", "rgba(255, 99, 99, 0.4)")
    elif importance == "Important":
        return ("rgba(255, 179, 71, 0.15)", "#FFB347", "rgba(255, 179, 71, 0.4)")
    else:
        return ("rgba(160, 160, 160, 0.15)", "#A0A0A0", "rgba(160, 160, 160, 0.4)")
