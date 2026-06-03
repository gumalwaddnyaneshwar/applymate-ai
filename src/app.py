"""
ApplyMate AI - Main Application
================================
Open Source Hackathon 2026 | Elite Coders
Author: Dnyaneshwar Gumalwad
"""

import streamlit as st
import time
import pandas as pd
import sys
import os
sys.path.append(os.path.dirname(__file__))

# ─── Page Config ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="ApplyMate AI — Job Application Assistant",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── Global CSS ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Syne:wght@400;600;700;800&display=swap');

html, body, [class*="css"] { font-family: 'Space Grotesk', sans-serif; }
#MainMenu, footer, header {visibility: hidden;}
.stDeployButton {display: none;}

.stApp {
    background: linear-gradient(135deg, #0F0F1A 0%, #1A1A2E 50%, #16213E 100%);
    min-height: 100vh;
}
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1A1A2E 0%, #0F0F1A 100%);
    border-right: 1px solid rgba(108, 99, 255, 0.2);
}
[data-testid="stSidebar"] * {color: #E8E8F0 !important;}

.hero-container { text-align: center; padding: 3rem 2rem 2rem; }
.hero-badge {
    display: inline-block; background: rgba(108, 99, 255, 0.15);
    border: 1px solid rgba(108, 99, 255, 0.4); color: #A89CFF;
    padding: 0.3rem 1rem; border-radius: 50px; font-size: 0.8rem;
    font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 1.2rem;
}
.hero-title {
    font-family: 'Syne', sans-serif; font-size: 3.2rem; font-weight: 800;
    background: linear-gradient(135deg, #FFFFFF 0%, #A89CFF 50%, #6C63FF 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    background-clip: text; line-height: 1.1; margin-bottom: 1rem;
}
.hero-subtitle {
    color: #9090B0; font-size: 1.1rem; max-width: 600px;
    margin: 0 auto 2rem; line-height: 1.6;
}
.stats-container {
    display: flex; justify-content: center; gap: 2rem;
    margin: 1.5rem 0 2.5rem; flex-wrap: wrap;
}
.stat-item { text-align: center; }
.stat-number { font-family: 'Syne', sans-serif; font-size: 1.8rem; font-weight: 800; color: #6C63FF; }
.stat-label { font-size: 0.75rem; color: #6060A0; text-transform: uppercase; letter-spacing: 0.08em; }
.feature-card {
    background: rgba(255,255,255,0.03); border: 1px solid rgba(108, 99, 255, 0.15);
    border-radius: 16px; padding: 1.5rem; text-align: center; height: 100%;
}
.feature-icon { font-size: 2rem; margin-bottom: 0.8rem; }
.feature-title { font-family: 'Syne', sans-serif; font-size: 1rem; font-weight: 700; color: #E8E8F0; margin-bottom: 0.5rem; }
.feature-desc { font-size: 0.85rem; color: #7070A0; line-height: 1.5; }
.section-header { font-family: 'Syne', sans-serif; font-size: 1.8rem; font-weight: 700; color: #E8E8F0; margin-bottom: 0.3rem; }
.section-sub { color: #7070A0; font-size: 0.95rem; margin-bottom: 1.5rem; }
.score-container {
    background: rgba(108, 99, 255, 0.08); border: 1px solid rgba(108, 99, 255, 0.3);
    border-radius: 20px; padding: 2rem; text-align: center; margin: 1rem 0;
}
.score-number { font-family: 'Syne', sans-serif; font-size: 4rem; font-weight: 800; line-height: 1; }
.score-label { font-size: 0.9rem; color: #7070A0; margin-top: 0.3rem; text-transform: uppercase; letter-spacing: 0.1em; }
.keyword-found {
    display: inline-block; background: rgba(72, 199, 142, 0.15);
    border: 1px solid rgba(72, 199, 142, 0.4); color: #48C78E;
    padding: 0.25rem 0.75rem; border-radius: 50px; font-size: 0.8rem; margin: 0.2rem; font-weight: 500;
}
.keyword-missing {
    display: inline-block; background: rgba(255, 99, 99, 0.15);
    border: 1px solid rgba(255, 99, 99, 0.4); color: #FF6363;
    padding: 0.25rem 0.75rem; border-radius: 50px; font-size: 0.8rem; margin: 0.2rem; font-weight: 500;
}
.result-card {
    background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08);
    border-radius: 12px; padding: 1.2rem 1.5rem; margin-bottom: 1rem;
}
.custom-divider {
    height: 1px; background: linear-gradient(90deg, transparent, rgba(108,99,255,0.3), transparent);
    margin: 2rem 0;
}
.stButton > button {
    background: linear-gradient(135deg, #6C63FF, #A89CFF); color: white;
    border: none; border-radius: 10px; padding: 0.6rem 2rem;
    font-family: 'Space Grotesk', sans-serif; font-weight: 600; font-size: 0.95rem; width: 100%;
}
.stTextArea textarea, .stTextInput input {
    background: rgba(255,255,255,0.05) !important; border: 1px solid rgba(108, 99, 255, 0.2) !important;
    border-radius: 10px !important; color: #E8E8F0 !important;
}
.footer {
    text-align: center; padding: 2rem; color: #404060; font-size: 0.8rem;
    border-top: 1px solid rgba(255,255,255,0.05); margin-top: 3rem;
}
.kw-card {
    background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08);
    border-radius: 12px; padding: 1rem 1.2rem; margin-bottom: 0.8rem;
}
.priority-badge {
    display: inline-block; padding: 0.2rem 0.6rem; border-radius: 50px;
    font-size: 0.72rem; font-weight: 600; margin-left: 0.5rem;
}
.summary-box {
    background: rgba(108, 99, 255, 0.08); border: 1px solid rgba(108, 99, 255, 0.25);
    border-radius: 14px; padding: 1.2rem 1.5rem; margin: 1rem 0;
}
</style>
""", unsafe_allow_html=True)

# ─── Sidebar ────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='text-align:center; padding: 1rem 0 1.5rem;'>
        <div style='font-family:Syne,sans-serif; font-size:1.4rem; font-weight:800;
                    background:linear-gradient(135deg,#fff,#A89CFF);
                    -webkit-background-clip:text; -webkit-text-fill-color:transparent;'>
            🎯 ApplyMate AI
        </div>
        <div style='color:#505080; font-size:0.75rem; margin-top:0.3rem;'>
            OSH 2026 · Elite Coders
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    page = st.radio("Navigate", [
        "🏠  Home", "📊  ATS Score Analyzer", "🔑  Keyword Analysis",
        "✍️  Cover Letter", "📈  Skill Roadmap", "🎤  Interview Prep"
    ], label_visibility="collapsed")
    st.markdown("---")
    st.markdown("""
    <div style='font-size:0.8rem; color:#505080;'>
        <div style='font-weight:600; color:#7070A0; margin-bottom:0.5rem;'>HOW IT WORKS</div>
        <div style='margin-bottom:0.4rem;'>① Upload your Resume (PDF)</div>
        <div style='margin-bottom:0.4rem;'>② Paste the Job Description</div>
        <div style='margin-bottom:0.4rem;'>③ Click Analyze</div>
        <div>④ Apply with confidence 🚀</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("""
    <div style='font-size:0.75rem; color:#404060; text-align:center;'>
        ✅ 100% Free &nbsp;·&nbsp; ✅ No Account<br>
        ✅ Open Source &nbsp;·&nbsp; ✅ Privacy First
    </div>
    """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
# HOME PAGE
# ════════════════════════════════════════════════════════════════════════════
if "🏠" in page:
    st.markdown("""
    <div class='hero-container'>
        <div class='hero-badge'>🏆 Open Source Hackathon 2026 · Elite Coders</div>
        <div class='hero-title'>Your AI-Powered<br>Job Application Assistant</div>
        <div class='hero-subtitle'>
            Paste a Job Description + Resume → Get ATS Score, Keyword Fixes,
            Cover Letter, Skill Gap Roadmap & Interview Questions.<br>
            <strong style='color:#A89CFF;'>All free. No account. No data stored.</strong>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='stats-container'>
        <div class='stat-item'><div class='stat-number'>5-in-1</div><div class='stat-label'>AI Modules</div></div>
        <div class='stat-item'><div class='stat-number'>100%</div><div class='stat-label'>Free Forever</div></div>
        <div class='stat-item'><div class='stat-number'>0</div><div class='stat-label'>Data Stored</div></div>
        <div class='stat-item'><div class='stat-number'>MIT</div><div class='stat-label'>Open Source</div></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='custom-divider'></div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align:center; font-family:Syne,sans-serif; font-size:1.5rem; font-weight:700; color:#E8E8F0; margin-bottom:1.5rem;'>Everything You Need to Land the Job</div>", unsafe_allow_html=True)

    cols = st.columns(5)
    features = [
        ("📊", "ATS Score", "Know your score before the recruiter even sees it"),
        ("🔑", "Keyword Gap", "AI-powered keyword gap detection with priority ranking"),
        ("✍️", "Cover Letter", "AI-tailored cover letter for every JD"),
        ("📈", "Skill Roadmap", "Know what to learn and how fast"),
        ("🎤", "Interview Prep", "Role-specific Q&A so you're never caught off guard"),
    ]
    for col, (icon, title, desc) in zip(cols, features):
        with col:
            st.markdown(f"""
            <div class='feature-card'>
                <div class='feature-icon'>{icon}</div>
                <div class='feature-title'>{title}</div>
                <div class='feature-desc'>{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<div class='custom-divider'></div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align:center; font-family:Syne,sans-serif; font-size:1.5rem; font-weight:700; color:#E8E8F0; margin-bottom:1rem;'>Why ApplyMate AI?</div>", unsafe_allow_html=True)

    _, col_mid, _ = st.columns([1, 2, 1])
    with col_mid:
        df = pd.DataFrame({
            "Feature": ["ATS Score", "AI Keyword Analysis", "Cover Letter", "Interview Prep", "Skill Roadmap", "100% Free", "Open Source", "No Data Stored"],
            "Jobscan": ["✅", "❌", "❌", "❌", "❌", "❌", "❌", "❌"],
            "Others": ["✅", "❌", "❌", "❌", "❌", "❌", "❌", "❌"],
            "ApplyMate AI 🎯": ["✅", "✅", "✅", "✅", "✅", "✅", "✅", "✅"],
        })
        st.dataframe(df, hide_index=True, use_container_width=True)

    st.markdown("""
    <div class='footer'>
        Built with ❤️ by <strong>Dnyaneshwar Gumalwad</strong> ·
        Open Source Hackathon 2026 · Elite Coders ·
        <a href='https://github.com/gumalwaddnyaneshwar/applymate-ai' style='color:#6C63FF;'>GitHub</a>
    </div>
    """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
# ATS SCORE PAGE
# ════════════════════════════════════════════════════════════════════════════
elif "📊" in page:
    from ats_scorer import calculate_ats_score
    from utils import extract_text_from_pdf

    st.markdown("<div class='section-header'>📊 ATS Score Analyzer</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-sub'>Upload your resume and paste the job description to get your ATS compatibility score.</div>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1], gap="large")
    with col1:
        st.markdown("**📄 Upload Your Resume (PDF)**")
        uploaded_file = st.file_uploader("Resume", type=["pdf"], label_visibility="collapsed")
        st.markdown("**📋 Paste Job Description**")
        jd_text = st.text_area("JD", placeholder="Paste the full job description here...", height=280, label_visibility="collapsed")
        analyze_btn = st.button("🚀 Analyze My Resume", use_container_width=True)

    with col2:
        if analyze_btn:
            if not uploaded_file or not jd_text.strip():
                st.error("⚠️ Please upload your resume and paste the job description.")
            else:
                with st.spinner("🤖 Analyzing your resume..."):
                    time.sleep(1)
                    resume_text = extract_text_from_pdf(uploaded_file)
                    results = calculate_ats_score(resume_text, jd_text)

                score = results["score"]
                color = "#48C78E" if score >= 70 else "#FFB347" if score >= 40 else "#FF6363"
                label = "Excellent Match!" if score >= 70 else "Needs Improvement" if score >= 40 else "Poor Match"

                st.markdown(f"""
                <div class='score-container'>
                    <div class='score-number' style='color:{color};'>{score}</div>
                    <div style='font-size:1rem; color:{color}; font-weight:600; margin-top:0.3rem;'>{label}</div>
                    <div class='score-label'>ATS Compatibility Score / 100</div>
                </div>
                """, unsafe_allow_html=True)
                st.progress(score / 100)

                st.markdown("**✅ Keywords Found**")
                found_html = "".join([f"<span class='keyword-found'>{k}</span>" for k in results["found_keywords"]])
                st.markdown(f"<div style='margin-bottom:1rem;'>{found_html}</div>", unsafe_allow_html=True)

                st.markdown("**❌ Missing Keywords**")
                missing_html = "".join([f"<span class='keyword-missing'>{k}</span>" for k in results["missing_keywords"]])
                st.markdown(f"<div style='margin-bottom:1rem;'>{missing_html}</div>", unsafe_allow_html=True)

                st.markdown("**💡 Quick Tips**")
                for tip in results["tips"]:
                    st.markdown(f"<div class='result-card'><div style='color:#E8E8F0; font-size:0.9rem;'>💡 {tip}</div></div>", unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style='text-align:center; padding:4rem 2rem; color:#404060;'>
                <div style='font-size:3rem; margin-bottom:1rem;'>📊</div>
                <div style='font-size:1rem; color:#505080;'>Upload your resume and paste a JD to see your score.</div>
            </div>
            """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
# KEYWORD ANALYSIS PAGE — AI POWERED
# ════════════════════════════════════════════════════════════════════════════
elif "🔑" in page:
    from keyword_analyzer import analyze_keywords_with_ai, get_importance_color
    from utils import extract_text_from_pdf

    st.markdown("<div class='section-header'>🔑 AI Keyword Gap Analyzer</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-sub'>Powered by Google Gemini AI — smarter, deeper keyword analysis with priority ranking.</div>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1], gap="large")
    with col1:
        st.markdown("**📄 Upload Your Resume (PDF)**")
        uploaded_file = st.file_uploader("Resume", type=["pdf"], label_visibility="collapsed", key="kw_resume")
        st.markdown("**📋 Paste Job Description**")
        jd_text = st.text_area("JD", placeholder="Paste the full job description here...", height=280, label_visibility="collapsed", key="kw_jd")
        analyze_btn = st.button("🤖 Analyze with AI", use_container_width=True)

    with col2:
        if analyze_btn:
            if not uploaded_file or not jd_text.strip():
                st.error("⚠️ Please upload your resume and paste the job description.")
            else:
                with st.spinner("🤖 Gemini AI is analyzing your resume... (15-20 seconds)"):
                    resume_text = extract_text_from_pdf(uploaded_file)
                    results = analyze_keywords_with_ai(resume_text, jd_text)

                if results:
                    # Match Score
                    score = results.get("match_percentage", 0)
                    color = "#48C78E" if score >= 70 else "#FFB347" if score >= 40 else "#FF6363"
                    label = "Excellent Match!" if score >= 70 else "Needs Improvement" if score >= 40 else "Poor Match"

                    st.markdown(f"""
                    <div class='score-container'>
                        <div class='score-number' style='color:{color};'>{score}</div>
                        <div style='font-size:1rem; color:{color}; font-weight:600; margin-top:0.3rem;'>{label}</div>
                        <div class='score-label'>AI Match Score / 100</div>
                    </div>
                    """, unsafe_allow_html=True)
                    st.progress(score / 100)

                    # AI Summary
                    summary = results.get("summary", "")
                    if summary:
                        st.markdown(f"""
                        <div class='summary-box'>
                            <div style='font-size:0.8rem; color:#A89CFF; font-weight:600; margin-bottom:0.4rem;'>🤖 AI ANALYSIS</div>
                            <div style='color:#E8E8F0; font-size:0.9rem; line-height:1.6;'>{summary}</div>
                        </div>
                        """, unsafe_allow_html=True)

                    # Top 3 Priorities
                    priorities = results.get("top_3_priorities", [])
                    if priorities:
                        st.markdown("**🎯 Top 3 Action Items**")
                        for i, p in enumerate(priorities, 1):
                            st.markdown(f"""
                            <div class='result-card'>
                                <span style='color:#6C63FF; font-weight:700;'>#{i}</span>
                                <span style='color:#E8E8F0; font-size:0.9rem; margin-left:0.5rem;'>{p}</span>
                            </div>
                            """, unsafe_allow_html=True)

                    # Found Keywords
                    found = results.get("found_keywords", [])
                    if found:
                        st.markdown(f"**✅ Keywords Found ({len(found)})**")
                        found_html = "".join([f"<span class='keyword-found'>{k['keyword']} <small>({k['category']})</small></span>" for k in found])
                        st.markdown(f"<div style='margin-bottom:1rem;'>{found_html}</div>", unsafe_allow_html=True)

                    # Missing Keywords with suggestions
                    missing = results.get("missing_keywords", [])
                    if missing:
                        st.markdown(f"**❌ Missing Keywords ({len(missing)}) — With Suggestions**")
                        for kw in missing:
                            bg, text_color, border = get_importance_color(kw.get("importance", "Optional"))
                            st.markdown(f"""
                            <div class='kw-card'>
                                <div style='display:flex; align-items:center; margin-bottom:0.4rem;'>
                                    <span style='color:#FF6363; font-weight:600;'>{kw['keyword']}</span>
                                    <span class='priority-badge' style='background:{bg}; color:{text_color}; border:1px solid {border};'>
                                        {kw.get('importance','Optional')}
                                    </span>
                                    <span style='color:#505080; font-size:0.78rem; margin-left:0.5rem;'>· {kw.get('category','')}</span>
                                </div>
                                <div style='color:#7070A0; font-size:0.82rem;'>💡 {kw.get('suggestion','')}</div>
                            </div>
                            """, unsafe_allow_html=True)
                else:
                    st.error("AI analysis failed. Please try again.")
        else:
            st.markdown("""
            <div style='text-align:center; padding:4rem 2rem; color:#404060;'>
                <div style='font-size:3rem; margin-bottom:1rem;'>🤖</div>
                <div style='font-size:1rem; color:#505080;'>
                    Gemini AI will analyze your resume<br>and give smart keyword suggestions.
                </div>
            </div>
            """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
# COMING SOON PAGES
# ════════════════════════════════════════════════════════════════════════════
else:
    module_info = {
        "✍️": ("Cover Letter Generator", "Day 4", "AI-tailored cover letter for every job description"),
        "📈": ("Skill Roadmap", "Day 5", "Personalized learning path with free resources"),
        "🎤": ("Interview Prep", "Day 5", "Role-specific Q&A with model answers"),
    }
    for key, (name, day, desc) in module_info.items():
        if key in page:
            st.markdown(f"""
            <div style='text-align:center; padding:5rem 2rem;'>
                <div style='font-size:4rem; margin-bottom:1rem;'>{key}</div>
                <div class='section-header'>{name}</div>
                <div class='section-sub'>{desc}</div>
                <div style='margin-top:2rem; display:inline-block;
                            background:rgba(108,99,255,0.1); border:1px solid rgba(108,99,255,0.3);
                            color:#A89CFF; padding:0.5rem 1.5rem; border-radius:50px;
                            font-size:0.85rem; font-weight:600;'>
                    🚧 Building Now · Launching {day}
                </div>
            </div>
            """, unsafe_allow_html=True)
            break
