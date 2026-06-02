"""
ApplyMate AI - ATS Scoring Engine
===================================
Calculates ATS compatibility score between resume and job description.
Uses keyword matching + section detection + formatting checks.
"""

import re
from collections import Counter


# ─── Common Technical Keywords by Category ───────────────────────────────────
TECH_KEYWORDS = [
    # Programming Languages
    "python", "java", "javascript", "typescript", "c++", "c#", "r", "scala", "go", "rust",
    # ML/AI
    "machine learning", "deep learning", "neural network", "nlp", "computer vision",
    "tensorflow", "pytorch", "keras", "scikit-learn", "huggingface", "transformers",
    "llm", "rag", "langchain", "openai", "gemini", "bert", "gpt",
    # Data
    "pandas", "numpy", "matplotlib", "seaborn", "sql", "mongodb", "postgresql",
    "data analysis", "data science", "feature engineering", "eda",
    # Web/API
    "fastapi", "flask", "django", "react", "node.js", "rest api", "graphql",
    # DevOps/Cloud
    "docker", "kubernetes", "aws", "gcp", "azure", "git", "github", "ci/cd",
    # Soft Skills
    "communication", "teamwork", "problem solving", "leadership", "collaboration",
]

RESUME_SECTIONS = [
    "experience", "education", "skills", "projects", "certifications",
    "summary", "objective", "achievements", "publications"
]


def extract_keywords(text: str) -> list[str]:
    """Extract meaningful keywords from text."""
    text = text.lower()
    # Remove special characters but keep spaces
    text = re.sub(r'[^\w\s\.\+#]', ' ', text)
    found = []
    for keyword in TECH_KEYWORDS:
        if keyword in text:
            found.append(keyword)
    # Also extract single capitalized words (likely tech terms)
    words = text.split()
    for word in words:
        word = word.strip('.,;:()[]')
        if len(word) > 2 and word.isalpha():
            found.append(word)
    return list(set(found))


def extract_jd_keywords(jd_text: str) -> list[str]:
    """Extract important keywords specifically from a job description."""
    jd_lower = jd_text.lower()
    found_keywords = []

    # Match known tech keywords
    for keyword in TECH_KEYWORDS:
        if keyword in jd_lower:
            found_keywords.append(keyword)

    # Extract words after common JD patterns
    patterns = [
        r'experience (?:with|in) ([a-zA-Z\s,+#]+?)(?:\.|,|\n|and)',
        r'proficiency in ([a-zA-Z\s,+#]+?)(?:\.|,|\n)',
        r'knowledge of ([a-zA-Z\s,+#]+?)(?:\.|,|\n)',
        r'familiarity with ([a-zA-Z\s,+#]+?)(?:\.|,|\n)',
        r'skills?: ([a-zA-Z\s,+#]+?)(?:\.|,|\n)',
    ]
    for pattern in patterns:
        matches = re.findall(pattern, jd_lower)
        for match in matches:
            words = [w.strip() for w in match.split(',')]
            found_keywords.extend(words)

    return list(set([k.strip() for k in found_keywords if len(k.strip()) > 2]))


def check_resume_sections(resume_text: str) -> dict:
    """Check if resume has essential sections."""
    resume_lower = resume_text.lower()
    section_scores = {}
    for section in RESUME_SECTIONS:
        section_scores[section] = section in resume_lower
    return section_scores


def generate_tips(score: int, missing_keywords: list, section_scores: dict) -> list[str]:
    """Generate actionable improvement tips based on analysis."""
    tips = []

    if score < 40:
        tips.append("Your resume has very low keyword overlap with the job description. Tailor it specifically for this role.")

    if len(missing_keywords) > 5:
        top_missing = missing_keywords[:3]
        tips.append(f"Add these critical missing keywords naturally: {', '.join(top_missing)}")

    if not section_scores.get("summary") and not section_scores.get("objective"):
        tips.append("Add a professional summary section at the top that mirrors keywords from the JD.")

    if not section_scores.get("skills"):
        tips.append("Add a dedicated 'Skills' section listing your technical and soft skills.")

    if not section_scores.get("projects"):
        tips.append("Add a 'Projects' section to showcase hands-on experience with relevant technologies.")

    if score >= 70:
        tips.append("Great match! Focus on quantifying your achievements with numbers and metrics.")

    if score >= 40 and score < 70:
        tips.append("Decent match. Incorporate more JD-specific keywords in your experience bullet points.")

    tips.append("Use action verbs like 'developed', 'built', 'implemented', 'optimized' to strengthen bullet points.")
    tips.append("Keep resume to 1 page for fresher roles and ensure clean formatting for ATS readability.")

    return tips[:5]  # Return top 5 tips


def calculate_ats_score(resume_text: str, jd_text: str) -> dict:
    """
    Main function: Calculate ATS score and return full analysis.

    Returns:
        dict with keys: score, found_keywords, missing_keywords, tips, section_scores
    """
    if not resume_text or not jd_text:
        return {
            "score": 0,
            "found_keywords": [],
            "missing_keywords": [],
            "tips": ["Could not parse resume. Please ensure it's a text-based PDF."],
            "section_scores": {}
        }

    # Extract keywords from JD (what employer wants)
    jd_keywords = extract_jd_keywords(jd_text)

    # Extract keywords from resume (what candidate has)
    resume_keywords = extract_keywords(resume_text)
    resume_text_lower = resume_text.lower()

    # Find matches and gaps
    found_keywords = []
    missing_keywords = []

    for keyword in jd_keywords:
        if keyword in resume_text_lower:
            found_keywords.append(keyword)
        else:
            missing_keywords.append(keyword)

    # Remove duplicates and sort
    found_keywords = sorted(list(set(found_keywords)))
    missing_keywords = sorted(list(set(missing_keywords)))

    # Calculate base score from keyword overlap
    total_jd_keywords = len(jd_keywords)
    if total_jd_keywords == 0:
        keyword_score = 50
    else:
        keyword_score = int((len(found_keywords) / total_jd_keywords) * 70)

    # Section bonus (up to 20 points)
    section_scores = check_resume_sections(resume_text)
    section_bonus = sum(1 for v in section_scores.values() if v) * 2
    section_bonus = min(section_bonus, 20)

    # Length bonus (up to 10 points) — resume should have reasonable content
    word_count = len(resume_text.split())
    length_bonus = 10 if word_count > 200 else 5 if word_count > 100 else 0

    # Final score (capped at 100)
    final_score = min(keyword_score + section_bonus + length_bonus, 100)

    # Generate tips
    tips = generate_tips(final_score, missing_keywords, section_scores)

    return {
        "score": final_score,
        "found_keywords": found_keywords[:20],    # Top 20 found
        "missing_keywords": missing_keywords[:15], # Top 15 missing
        "tips": tips,
        "section_scores": section_scores
    }
