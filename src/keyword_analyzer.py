"""
ApplyMate AI - AI Keyword Gap Analyzer
========================================
Uses Google Gemini API for intelligent keyword extraction and gap analysis.
"""

import google.generativeai as genai
import streamlit as st
import json
import re


def configure_gemini():
    """Configure Gemini API with key from Streamlit secrets."""
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
        genai.configure(api_key=api_key)
        return genai.GenerativeModel("gemini-1.5-flash")
    except Exception as e:
        st.error("⚠️ Gemini API key not found. Please add it in Streamlit secrets.")
        return None


def analyze_keywords_with_ai(resume_text: str, jd_text: str) -> dict:
    """
    Use Gemini AI to intelligently analyze keyword gaps between resume and JD.
    Returns structured analysis with priority levels.
    """
    model = configure_gemini()
    if not model:
        return None

    prompt = f"""
You are an expert ATS (Applicant Tracking System) analyst and career coach.

Analyze the following Job Description and Resume carefully.

JOB DESCRIPTION:
{jd_text[:3000]}

RESUME:
{resume_text[:3000]}

Your task: Perform a detailed keyword gap analysis.

Return ONLY a valid JSON object with this exact structure (no markdown, no extra text):
{{
    "found_keywords": [
        {{"keyword": "python", "category": "Programming", "importance": "Critical"}},
        {{"keyword": "machine learning", "category": "AI/ML", "importance": "Critical"}}
    ],
    "missing_keywords": [
        {{"keyword": "docker", "category": "DevOps", "importance": "Important", "suggestion": "Add Docker experience in your projects section"}},
        {{"keyword": "communication", "category": "Soft Skills", "importance": "Optional", "suggestion": "Mention team collaboration in your internship description"}}
    ],
    "match_percentage": 72,
    "summary": "Your resume is a strong match for this role. Key strengths include your Python and ML experience. Focus on adding Docker and REST API keywords.",
    "top_3_priorities": ["Add Docker to skills", "Mention REST API experience", "Add communication examples"]
}}

Categories must be one of: Programming, AI/ML, Data Science, DevOps/Cloud, Web/API, Soft Skills, Domain Knowledge, Tools
Importance must be one of: Critical, Important, Optional
"""

    try:
        response = model.generate_content(prompt)
        raw = response.text.strip()

        # Clean markdown if present
        raw = re.sub(r'```json\s*', '', raw)
        raw = re.sub(r'```\s*', '', raw)
        raw = raw.strip()

        result = json.loads(raw)
        return result

    except json.JSONDecodeError:
        # Try to extract JSON from response
        try:
            json_match = re.search(r'\{.*\}', raw, re.DOTALL)
            if json_match:
                result = json.loads(json_match.group())
                return result
        except:
            pass
        return None
    except Exception as e:
        st.error(f"AI Analysis failed: {str(e)}")
        return None


def get_category_color(category: str) -> str:
    """Return color for each keyword category."""
    colors = {
        "Programming": "#6C63FF",
        "AI/ML": "#FF6584",
        "Data Science": "#48C78E",
        "DevOps/Cloud": "#FFB347",
        "Web/API": "#4FC3F7",
        "Soft Skills": "#CE93D8",
        "Domain Knowledge": "#80CBC4",
        "Tools": "#FFCC02",
    }
    return colors.get(category, "#A0A0A0")


def get_importance_color(importance: str) -> tuple:
    """Return background and text color for importance level."""
    if importance == "Critical":
        return ("rgba(255, 99, 99, 0.15)", "#FF6363", "rgba(255, 99, 99, 0.4)")
    elif importance == "Important":
        return ("rgba(255, 179, 71, 0.15)", "#FFB347", "rgba(255, 179, 71, 0.4)")
    else:
        return ("rgba(160, 160, 160, 0.15)", "#A0A0A0", "rgba(160, 160, 160, 0.4)")
