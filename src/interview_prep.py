"""
ApplyMate AI - Interview Prep Generator
========================================
Uses Google Gemini API to generate role-specific interview questions and answers.
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


def generate_interview_questions(resume_text: str, jd_text: str) -> dict:
    """Generate role-specific interview questions and model answers."""
    model = configure_gemini()
    if not model:
        return None

    prompt = f"""
You are an expert technical interviewer and career coach.

Based on the job description and resume below, generate targeted interview questions with model answers.

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
            "model_answer": "XGBoost handles imbalanced datasets through the scale_pos_weight parameter, which adjusts the weight of positive class samples. For example, if you have 99% negative and 1% positive, setting scale_pos_weight=99 balances the training. Additionally, you can use techniques like SMOTE for oversampling before training, which I implemented in my Credit Card Fraud Detection project achieving 97%+ ROC-AUC.",
            "tip": "Always connect your answer to a project you've done for extra impact."
        }},
        {{
            "question": "What is the difference between precision and recall?",
            "category": "ML Fundamentals",
            "difficulty": "Easy",
            "model_answer": "Precision measures how many of the predicted positives are actually positive (TP/TP+FP), while recall measures how many actual positives were correctly identified (TP/TP+FN). In fraud detection, recall is more important because missing a fraud (false negative) is costlier than a false alarm.",
            "tip": "Give a real-world use case to show you understand when to prioritize each."
        }}
    ],
    "hr_questions": [
        {{
            "question": "Tell me about yourself.",
            "model_answer": "I'm a final-year BCA student specializing in AI/ML at JSPM University, Pune. I've built two production-ready ML projects — a Credit Card Fraud Detection System achieving 97%+ ROC-AUC, and an AI Resume Analyzer using HuggingFace Transformers. I also published a research paper on CivicFix in IJARSCT. I'm passionate about building AI solutions that solve real problems and I'm excited about this opportunity at your company.",
            "tip": "Keep it under 2 minutes. End with why you're excited about this specific role."
        }},
        {{
            "question": "Why do you want to join this company?",
            "model_answer": "I've researched your company's work in AI and machine learning, and I'm impressed by the kind of real-world problems you solve. As someone who has built end-to-end ML pipelines from scratch, I believe I can contribute meaningfully from day one while continuing to grow under experienced mentors.",
            "tip": "Research the company beforehand and mention something specific about them."
        }}
    ],
    "project_questions": [
        {{
            "question": "Walk me through your Credit Card Fraud Detection project.",
            "model_answer": "I built an end-to-end ML pipeline on a dataset of 284,807 transactions with only 0.17% fraud cases — a highly imbalanced problem. I used SMOTE to oversample the minority class and trained Logistic Regression, Random Forest, and XGBoost. The final XGBoost model achieved 97%+ ROC-AUC. I also built a Streamlit interface for real-time predictions and documented everything on GitHub.",
            "tip": "Use the STAR format: Situation, Task, Action, Result. Always end with the impact/metric."
        }}
    ],
    "quick_tips": [
        "Research the company's tech stack before the interview",
        "Prepare 2-3 stories using STAR format from your projects",
        "Always ask thoughtful questions at the end of the interview",
        "For technical rounds, think out loud — interviewers want to see your thought process"
    ]
}}
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
        st.error(f"Interview prep generation failed: {str(e)}")
        return None
