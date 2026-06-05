"""
ApplyMate AI - Interview Prep Generator
========================================
Uses Groq (default) or Gemini (user key).
"""

import json
import re
import sys
import os
sys.path.append(os.path.dirname(__file__))
from ai_helper import ask_groq, ask_gemini


def generate_interview_questions(resume_text: str, jd_text: str, ai_mode: str = "groq", user_key: str = None) -> dict:
    prompt = f"""
You are an expert technical interviewer and career coach.
Generate targeted interview questions with model answers.

JOB DESCRIPTION:
{jd_text[:2500]}

RESUME:
{resume_text[:2500]}

Return ONLY a valid JSON object (no markdown, no extra text):
{{
    "role": "Machine Learning Engineer",
    "difficulty": "Fresher to Junior",
    "technical_questions": [
        {{
            "question": "Explain how XGBoost handles imbalanced datasets.",
            "category": "Machine Learning",
            "difficulty": "Medium",
            "model_answer": "XGBoost handles imbalanced datasets through the scale_pos_weight parameter which adjusts the weight of positive class samples. I implemented this in my Credit Card Fraud Detection project achieving 97%+ ROC-AUC.",
            "tip": "Always connect your answer to a project you have done."
        }},
        {{
            "question": "What is the difference between precision and recall?",
            "category": "ML Fundamentals",
            "difficulty": "Easy",
            "model_answer": "Precision measures how many predicted positives are actually positive (TP/TP+FP), while recall measures how many actual positives were correctly identified (TP/TP+FN). In fraud detection, recall is more important.",
            "tip": "Give a real-world use case to show understanding."
        }}
    ],
    "hr_questions": [
        {{
            "question": "Tell me about yourself.",
            "model_answer": "I am a final-year BCA student specializing in AI/ML at JSPM University, Pune. I built two production-ready ML projects and published a research paper in IJARSCT. I am passionate about building AI solutions that solve real problems.",
            "tip": "Keep it under 2 minutes. End with why you are excited about this specific role."
        }}
    ],
    "project_questions": [
        {{
            "question": "Walk me through your Credit Card Fraud Detection project.",
            "model_answer": "I built an end-to-end ML pipeline on 284,807 transactions with only 0.17% fraud cases. I used SMOTE to oversample the minority class and trained XGBoost achieving 97%+ ROC-AUC.",
            "tip": "Use STAR format: Situation, Task, Action, Result."
        }}
    ],
    "quick_tips": [
        "Research the company tech stack before the interview",
        "Prepare 2-3 stories using STAR format from your projects",
        "Always ask thoughtful questions at the end"
    ]
}}
"""
    if ai_mode == "gemini" and user_key:
        raw = ask_gemini(prompt, user_key, max_tokens=3000)
    else:
        raw = ask_groq(prompt, max_tokens=3000)

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
