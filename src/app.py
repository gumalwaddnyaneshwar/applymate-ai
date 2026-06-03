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

st.set_page_config(
    page_title="ApplyMate AI — Job Application Assistant",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Syne:wght@400;600;700;800&display=swap');
html, body, [class*="css"] { font-family: 'Space Grotesk', sans-serif; }
#MainMenu, footer, header {visibility: hidden;}
.stDeployButton {display: none;}
.stApp { background: linear-gradient(135deg, #0F0F1A 0%, #1A1A2E 50%, #16213E 100%); min-height: 100vh; }
[data-testid="stSidebar"] { background: linear-gradient(180deg, #1A1A2E 0%, #0F0F1A 100%); border-right: 1px solid rgba(108, 99, 255, 0.2); }
[data-testid="stSidebar"] * {color: #E8E8F0 !important;}
.hero-container { text-align: center; padding: 3rem 2rem 2rem; }
.hero-badge { display: inline-block; background: rgba(108, 99, 255, 0.15); border: 1px solid rgba(108, 99, 255, 0.4); color: #A89CFF; padding: 0.3rem 1rem; border-radius: 50px; font-size: 0.8rem; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 1.2rem; }
.hero-title { font-family: 'Syne', sans-serif; font-size: 3.2rem; font-weight: 800; background: linear-gradient(135deg, #FFFFFF 0%, #A89CFF 50%, #6C63FF 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; line-height: 1.1; margin-bottom: 1rem; }
.hero-subtitle { color: #9090B0; font-size: 1.1rem; max-width: 600px; margin: 0 auto 2rem; line-height: 1.6; }
.stats-container { display: flex; justify-content: center; gap: 2rem; margin: 1.5rem 0 2.5rem; flex-wrap: wrap; }
.stat-item { text-align: center; }
.stat-number { font-family: 'Syne', sans-serif; font-size: 1.8rem; font-weight: 800; color: #6C63FF; }
.stat-label { font-size: 0.75rem; color: #6060A0; text-transform: uppercase; letter-spacing: 0.08em; }
.feature-card { background: rgba(255,255,255,0.03); border: 1px solid rgba(108, 99, 255, 0.15); border-radius: 16px; padding: 1.5rem; text-align: center; height: 100%; }
.feature-icon { font-size: 2rem; margin-bottom: 0.8rem; }
.feature-title { font-family: 'Syne', sans-serif; font-size: 1rem; font-weight: 700; color: #E8E8F0; margin-bottom: 0.5rem; }
.feature-desc { font-size: 0.85rem; color: #7070A0; line-height: 1.5; }
.section-header { font-family: 'Syne', sans-serif; font-size: 1.8rem; font-weight: 700; color: #E8E8F0; margin-bottom: 0.3rem; }
.section-sub { color: #7070A0; font-size: 0.95rem; margin-bottom: 1.5rem; }
.score-container { background: rgba(108, 99, 255, 0.08); border: 1px solid rgba(108, 99, 255, 0.3); border-radius: 20px; padding: 2rem; text-align: center; margin: 1rem 0; }
.score-number { font-family: 'Syne', sans-serif; font-size: 4rem; font-weight: 800; line-height: 1; }
.score-label { font-size: 0.9rem; color: #7070A0; margin-top: 0.3rem; text-transform: uppercase; letter-spacing: 0.1em; }
.keyword-found { display: inline-block; background: rgba(72, 199, 142, 0.15); border: 1px solid rgba(72, 199, 142, 0.4); color: #48C78E; padding: 0.25rem 0.75rem; border-radius: 50px; font-size: 0.8rem; margin: 0.2rem; font-weight: 500; }
.keyword-missing { display: inline-block; background: rgba(255, 99, 99, 0.15); border: 1px solid rgba(255, 99, 99, 0.4); color: #FF6363; padding: 0.25rem 0.75rem; border-radius: 50px; font-size: 0.8rem; margin: 0.2rem; font-weight: 500; }
.result-card { background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 1.2rem 1.5rem; margin-bottom: 1rem; }
.result-card-title { font-weight: 600; color: #A89CFF; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 0.5rem; }
.custom-divider { height: 1px; background: linear-gradient(90deg, transparent, rgba(108,99,255,0.3), transparent); margin: 2rem 0; }
.stButton > button { background: linear-gradient(135deg, #6C63FF, #A89CFF); color: white; border: none; border-radius: 10px; padding: 0.6rem 2rem; font-family: 'Space Grotesk', sans-serif; font-weight: 600; font-size: 0.95rem; width: 100%; }
.stTextArea textarea, .stTextInput input { background: rgba(255,255,255,0.05) !important; border: 1px solid rgba(108, 99, 255, 0.2) !important; border-radius: 10px !important; color: #E8E8F0 !important; }
.footer { text-align: center; padding: 2rem; color: #404060; font-size: 0.8rem; border-top: 1px solid rgba(255,255,255,0.05); margin-top: 3rem; }
.kw-card { background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 1rem 1.2rem; margin-bottom: 0.8rem; }
.priority-badge { display: inline-block; padding: 0.2rem 0.6rem; border-radius: 50px; font-size: 0.72rem; font-weight: 600; margin-left: 0.5rem; }
.summary-box { background: rgba(108, 99, 255, 0.08); border: 1px solid rgba(108, 99, 255, 0.25); border-radius: 14px; padding: 1.2rem 1.5rem; margin: 1rem 0; }
.week-card { background: rgba(108,99,255,0.05); border: 1px solid rgba(108,99,255,0.2); border-radius: 12px; padding: 1rem 1.2rem; margin-bottom: 0.8rem; }
.q-card { background: rgba(255,255,255,0.03); border-left: 3px solid #6C63FF; border-radius: 0 12px 12px 0; padding: 1.2rem 1.5rem; margin-bottom: 1rem; }
.q-category { display: inline-block; background: rgba(108,99,255,0.15); color: #A89CFF; padding: 0.15rem 0.6rem; border-radius: 50px; font-size: 0.72rem; font-weight: 600; margin-bottom: 0.5rem; }
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
        <div style='color:#505080; font-size:0.75rem; margin-top:0.3rem;'>OSH 2026 · Elite Coders</div>
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
        ✅ 100% Free · ✅ No Account<br>✅ Open Source · ✅ Privacy First
    </div>
    """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
# HOME
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
        ("📈", "Skill Roadmap", "Personalized learning path with free resources"),
        ("🎤", "Interview Prep", "Role-specific Q&A so you're never caught off guard"),
    ]
    for col, (icon, title, desc) in zip(cols, features):
        with col:
            st.markdown(f"<div class='feature-card'><div class='feature-icon'>{icon}</div><div class='feature-title'>{title}</div><div class='feature-desc'>{desc}</div></div>", unsafe_allow_html=True)
    st.markdown("<div class='custom-divider'></div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align:center; font-family:Syne,sans-serif; font-size:1.5rem; font-weight:700; color:#E8E8F0; margin-bottom:1rem;'>Why ApplyMate AI?</div>", unsafe_allow_html=True)
    _, col_mid, _ = st.columns([1, 2, 1])
    with col_mid:
        df = pd.DataFrame({
            "Feature": ["ATS Score", "AI Keyword Analysis", "Cover Letter", "Interview Prep", "Skill Roadmap", "100% Free", "Open Source", "No Data Stored"],
            "Jobscan": ["✅","❌","❌","❌","❌","❌","❌","❌"],
            "Others": ["✅","❌","❌","❌","❌","❌","❌","❌"],
            "ApplyMate AI 🎯": ["✅","✅","✅","✅","✅","✅","✅","✅"],
        })
        st.dataframe(df, hide_index=True, use_container_width=True)
    st.markdown("<div class='footer'>Built with ❤️ by <strong>Dnyaneshwar Gumalwad</strong> · OSH 2026 · Elite Coders · <a href='https://github.com/gumalwaddnyaneshwar/applymate-ai' style='color:#6C63FF;'>GitHub</a></div>", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
# ATS SCORE
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
                st.markdown(f"<div class='score-container'><div class='score-number' style='color:{color};'>{score}</div><div style='font-size:1rem; color:{color}; font-weight:600; margin-top:0.3rem;'>{label}</div><div class='score-label'>ATS Compatibility Score / 100</div></div>", unsafe_allow_html=True)
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
            st.markdown("<div style='text-align:center; padding:4rem 2rem;'><div style='font-size:3rem;'>📊</div><div style='color:#505080;'>Upload your resume and paste a JD to see your score.</div></div>", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
# KEYWORD ANALYSIS
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
                with st.spinner("🤖 Gemini AI is analyzing... (15-20 seconds)"):
                    resume_text = extract_text_from_pdf(uploaded_file)
                    results = analyze_keywords_with_ai(resume_text, jd_text)
                if results:
                    score = results.get("match_percentage", 0)
                    color = "#48C78E" if score >= 70 else "#FFB347" if score >= 40 else "#FF6363"
                    label = "Excellent Match!" if score >= 70 else "Needs Improvement" if score >= 40 else "Poor Match"
                    st.markdown(f"<div class='score-container'><div class='score-number' style='color:{color};'>{score}</div><div style='font-size:1rem; color:{color}; font-weight:600;'>{label}</div><div class='score-label'>AI Match Score / 100</div></div>", unsafe_allow_html=True)
                    st.progress(score / 100)
                    summary = results.get("summary", "")
                    if summary:
                        st.markdown(f"<div class='summary-box'><div style='font-size:0.8rem; color:#A89CFF; font-weight:600; margin-bottom:0.4rem;'>🤖 AI ANALYSIS</div><div style='color:#E8E8F0; font-size:0.9rem; line-height:1.6;'>{summary}</div></div>", unsafe_allow_html=True)
                    priorities = results.get("top_3_priorities", [])
                    if priorities:
                        st.markdown("**🎯 Top 3 Action Items**")
                        for i, p in enumerate(priorities, 1):
                            st.markdown(f"<div class='result-card'><span style='color:#6C63FF; font-weight:700;'>#{i}</span> <span style='color:#E8E8F0; font-size:0.9rem;'>{p}</span></div>", unsafe_allow_html=True)
                    found = results.get("found_keywords", [])
                    if found:
                        st.markdown(f"**✅ Keywords Found ({len(found)})**")
                        found_html = "".join([f"<span class='keyword-found'>{k['keyword']} <small>({k['category']})</small></span>" for k in found])
                        st.markdown(f"<div style='margin-bottom:1rem;'>{found_html}</div>", unsafe_allow_html=True)
                    missing = results.get("missing_keywords", [])
                    if missing:
                        st.markdown(f"**❌ Missing Keywords ({len(missing)})**")
                        for kw in missing:
                            bg, text_color, border = get_importance_color(kw.get("importance", "Optional"))
                            st.markdown(f"<div class='kw-card'><div style='margin-bottom:0.4rem;'><span style='color:#FF6363; font-weight:600;'>{kw['keyword']}</span><span class='priority-badge' style='background:{bg}; color:{text_color}; border:1px solid {border};'>{kw.get('importance','Optional')}</span><span style='color:#505080; font-size:0.78rem; margin-left:0.5rem;'>· {kw.get('category','')}</span></div><div style='color:#7070A0; font-size:0.82rem;'>💡 {kw.get('suggestion','')}</div></div>", unsafe_allow_html=True)
                else:
                    st.error("AI analysis failed. Quota may be exceeded. Please try again later.")
        else:
            st.markdown("<div style='text-align:center; padding:4rem 2rem;'><div style='font-size:3rem;'>🤖</div><div style='color:#505080;'>Gemini AI will analyze your resume and give smart keyword suggestions.</div></div>", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
# COVER LETTER
# ════════════════════════════════════════════════════════════════════════════
elif "✍️" in page:
    from cover_letter import generate_cover_letter
    from utils import extract_text_from_pdf
    st.markdown("<div class='section-header'>✍️ AI Cover Letter Generator</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-sub'>Powered by Google Gemini AI — get a tailored cover letter for every job in seconds.</div>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1], gap="large")
    with col1:
        st.markdown("**📄 Upload Your Resume (PDF)**")
        uploaded_file = st.file_uploader("Resume", type=["pdf"], label_visibility="collapsed", key="cl_resume")
        st.markdown("**📋 Paste Job Description**")
        jd_text = st.text_area("JD", placeholder="Paste the full job description here...", height=180, label_visibility="collapsed", key="cl_jd")
        st.markdown("**👤 Your Details (Optional)**")
        user_name = st.text_input("Your Full Name", placeholder="Dnyaneshwar Gumalwad")
        company_name = st.text_input("Company Name", placeholder="GlobalLogic India")
        role_name = st.text_input("Role Applying For", placeholder="Machine Learning Engineer")
        generate_btn = st.button("✍️ Generate Cover Letter", use_container_width=True)
    with col2:
        if generate_btn:
            if not uploaded_file or not jd_text.strip():
                st.error("⚠️ Please upload your resume and paste the job description.")
            else:
                with st.spinner("✍️ Gemini AI is writing your cover letter... (15-20 seconds)"):
                    resume_text = extract_text_from_pdf(uploaded_file)
                    result = generate_cover_letter(resume_text, jd_text, user_name, company_name, role_name)
                if result:
                    subject = result.get("subject_line", "")
                    if subject:
                        st.markdown(f"<div class='result-card'><div class='result-card-title'>📧 EMAIL SUBJECT LINE</div><div style='color:#E8E8F0; font-size:0.95rem; font-weight:500;'>{subject}</div></div>", unsafe_allow_html=True)
                    cover_letter = result.get("cover_letter", "")
                    if cover_letter:
                        st.markdown("**📝 Your Tailored Cover Letter**")
                        st.markdown(f"<div style='background:rgba(255,255,255,0.03); border:1px solid rgba(108,99,255,0.2); border-radius:14px; padding:1.5rem; color:#E8E8F0; font-size:0.9rem; line-height:1.8; white-space:pre-line;'>{cover_letter}</div>", unsafe_allow_html=True)
                        st.text_area("📋 Copy from here:", value=cover_letter, height=250, key="copy_cl")
                    key_points = result.get("key_points_used", [])
                    if key_points:
                        st.markdown("**✅ Key Strengths Highlighted**")
                        for point in key_points:
                            st.markdown(f"<div class='result-card'><span style='color:#48C78E;'>✓</span> <span style='color:#E8E8F0; font-size:0.9rem;'>{point}</span></div>", unsafe_allow_html=True)
                    tips = result.get("tips", [])
                    if tips:
                        st.markdown("**💡 Pro Tips**")
                        for tip in tips:
                            st.markdown(f"<div class='result-card'><span style='color:#FFB347;'>💡</span> <span style='color:#E8E8F0; font-size:0.9rem;'>{tip}</span></div>", unsafe_allow_html=True)
                else:
                    st.error("Cover letter generation failed. API quota may be exceeded. Try again later.")
        else:
            st.markdown("<div style='text-align:center; padding:4rem 2rem;'><div style='font-size:3rem;'>✍️</div><div style='color:#505080;'>Fill in your details and click Generate to get your AI-written cover letter.</div></div>", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
# SKILL ROADMAP
# ════════════════════════════════════════════════════════════════════════════
elif "📈" in page:
    from skill_roadmap import generate_skill_roadmap
    from utils import extract_text_from_pdf
    st.markdown("<div class='section-header'>📈 Skill Gap Roadmap</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-sub'>Powered by Gemini AI — get a personalized week-by-week learning plan with free resources.</div>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1], gap="large")
    with col1:
        st.markdown("**📄 Upload Your Resume (PDF)**")
        uploaded_file = st.file_uploader("Resume", type=["pdf"], label_visibility="collapsed", key="sr_resume")
        st.markdown("**📋 Paste Job Description**")
        jd_text = st.text_area("JD", placeholder="Paste the full job description here...", height=280, label_visibility="collapsed", key="sr_jd")
        generate_btn = st.button("📈 Generate My Roadmap", use_container_width=True)
    with col2:
        if generate_btn:
            if not uploaded_file or not jd_text.strip():
                st.error("⚠️ Please upload your resume and paste the job description.")
            else:
                with st.spinner("📈 Gemini AI is building your roadmap... (15-20 seconds)"):
                    resume_text = extract_text_from_pdf(uploaded_file)
                    result = generate_skill_roadmap(resume_text, jd_text)
                if result:
                    # Readiness Score
                    score = result.get("readiness_score", 0)
                    color = "#48C78E" if score >= 70 else "#FFB347" if score >= 40 else "#FF6363"
                    st.markdown(f"<div class='score-container'><div class='score-number' style='color:{color};'>{score}%</div><div style='color:#A89CFF; font-size:0.9rem; font-weight:600; margin-top:0.3rem;'>Job Readiness</div><div style='color:#505080; font-size:0.8rem;'>{result.get('current_level','')} → {result.get('target_level','')}</div></div>", unsafe_allow_html=True)
                    st.progress(score / 100)

                    # Overall tip
                    tip = result.get("overall_tip", "")
                    if tip:
                        st.markdown(f"<div class='summary-box'><div style='font-size:0.8rem; color:#A89CFF; font-weight:600; margin-bottom:0.4rem;'>🤖 AI ASSESSMENT</div><div style='color:#E8E8F0; font-size:0.9rem; line-height:1.6;'>{tip}</div></div>", unsafe_allow_html=True)

                    # Skills you have
                    skills_have = result.get("skills_you_have", [])
                    if skills_have:
                        st.markdown("**✅ Skills You Already Have**")
                        found_html = "".join([f"<span class='keyword-found'>{s['skill']} ({s['level']})</span>" for s in skills_have])
                        st.markdown(f"<div style='margin-bottom:1rem;'>{found_html}</div>", unsafe_allow_html=True)

                    # Skills to learn
                    skills_learn = result.get("skills_to_learn", [])
                    if skills_learn:
                        st.markdown("**📚 Skills to Learn (With Free Resources)**")
                        for skill in skills_learn:
                            priority = skill.get("priority", "Medium")
                            p_color = "#FF6363" if priority == "High" else "#FFB347" if priority == "Medium" else "#A0A0A0"
                            st.markdown(f"""
                            <div class='kw-card'>
                                <div style='margin-bottom:0.5rem;'>
                                    <span style='color:#E8E8F0; font-weight:600; font-size:0.95rem;'>{skill['skill']}</span>
                                    <span class='priority-badge' style='background:rgba(255,99,99,0.1); color:{p_color}; border:1px solid {p_color};'>{priority} Priority</span>
                                    <span style='color:#505080; font-size:0.78rem; margin-left:0.5rem;'>⏱ {skill.get('time_to_learn','')}</span>
                                </div>
                                <div style='color:#7070A0; font-size:0.82rem; margin-bottom:0.5rem;'>📝 {skill.get('how_to_add_to_resume','')}</div>
                                <div style='font-size:0.8rem; color:#6C63FF; font-weight:600; margin-bottom:0.3rem;'>Free Resources:</div>
                                {"".join([f'<div style=\"margin-left:0.5rem;\"><a href=\"{r[\"url\"]}\" target=\"_blank\" style=\"color:#A89CFF; font-size:0.8rem;\">🔗 {r[\"name\"]}</a></div>' for r in skill.get('free_resources', [])])}
                            </div>
                            """, unsafe_allow_html=True)

                    # Week by week plan
                    plan = result.get("week_by_week_plan", [])
                    if plan:
                        st.markdown("**🗓️ Week-by-Week Action Plan**")
                        for week in plan:
                            st.markdown(f"""
                            <div class='week-card'>
                                <div style='color:#6C63FF; font-weight:700; font-size:0.85rem; margin-bottom:0.3rem;'>WEEK {week['week']}</div>
                                <div style='color:#E8E8F0; font-size:0.9rem; margin-bottom:0.3rem;'>{week['focus']}</div>
                                <div style='color:#48C78E; font-size:0.8rem;'>🎯 Goal: {week['goal']}</div>
                            </div>
                            """, unsafe_allow_html=True)
                else:
                    st.error("Roadmap generation failed. API quota may be exceeded. Try again later.")
        else:
            st.markdown("<div style='text-align:center; padding:4rem 2rem;'><div style='font-size:3rem;'>📈</div><div style='color:#505080;'>Upload your resume and paste a JD to get your personalized learning roadmap.</div></div>", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
# INTERVIEW PREP
# ════════════════════════════════════════════════════════════════════════════
elif "🎤" in page:
    from interview_prep import generate_interview_questions
    from utils import extract_text_from_pdf
    st.markdown("<div class='section-header'>🎤 Interview Prep</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-sub'>Powered by Gemini AI — role-specific questions with model answers so you're never caught off guard.</div>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1], gap="large")
    with col1:
        st.markdown("**📄 Upload Your Resume (PDF)**")
        uploaded_file = st.file_uploader("Resume", type=["pdf"], label_visibility="collapsed", key="ip_resume")
        st.markdown("**📋 Paste Job Description**")
        jd_text = st.text_area("JD", placeholder="Paste the full job description here...", height=280, label_visibility="collapsed", key="ip_jd")
        generate_btn = st.button("🎤 Generate Interview Questions", use_container_width=True)
    with col2:
        if generate_btn:
            if not uploaded_file or not jd_text.strip():
                st.error("⚠️ Please upload your resume and paste the job description.")
            else:
                with st.spinner("🎤 Gemini AI is preparing your interview questions... (15-20 seconds)"):
                    resume_text = extract_text_from_pdf(uploaded_file)
                    result = generate_interview_questions(resume_text, jd_text)
                if result:
                    st.markdown(f"<div class='summary-box'><div style='font-size:0.8rem; color:#A89CFF; font-weight:600; margin-bottom:0.3rem;'>🎯 INTERVIEW PROFILE</div><div style='color:#E8E8F0; font-size:0.9rem;'>Role: <strong>{result.get('role','')}</strong> · Level: <strong>{result.get('difficulty','')}</strong></div></div>", unsafe_allow_html=True)

                    # Technical Questions
                    tech_qs = result.get("technical_questions", [])
                    if tech_qs:
                        st.markdown("**💻 Technical Questions**")
                        for i, q in enumerate(tech_qs, 1):
                            with st.expander(f"Q{i}: {q['question']}"):
                                st.markdown(f"<span class='q-category'>{q.get('category','')}</span> <span class='q-category'>{q.get('difficulty','')}</span>", unsafe_allow_html=True)
                                st.markdown(f"**Model Answer:**\n\n{q.get('model_answer','')}")
                                st.info(f"💡 Tip: {q.get('tip','')}")

                    # HR Questions
                    hr_qs = result.get("hr_questions", [])
                    if hr_qs:
                        st.markdown("**🤝 HR / Behavioral Questions**")
                        for i, q in enumerate(hr_qs, 1):
                            with st.expander(f"Q{i}: {q['question']}"):
                                st.markdown(f"**Model Answer:**\n\n{q.get('model_answer','')}")
                                st.info(f"💡 Tip: {q.get('tip','')}")

                    # Project Questions
                    proj_qs = result.get("project_questions", [])
                    if proj_qs:
                        st.markdown("**🚀 Project-Based Questions**")
                        for i, q in enumerate(proj_qs, 1):
                            with st.expander(f"Q{i}: {q['question']}"):
                                st.markdown(f"**Model Answer:**\n\n{q.get('model_answer','')}")
                                st.info(f"💡 Tip: {q.get('tip','')}")

                    # Quick Tips
                    tips = result.get("quick_tips", [])
                    if tips:
                        st.markdown("**⚡ Quick Interview Tips**")
                        for tip in tips:
                            st.markdown(f"<div class='result-card'><span style='color:#FFB347;'>⚡</span> <span style='color:#E8E8F0; font-size:0.9rem;'>{tip}</span></div>", unsafe_allow_html=True)
                else:
                    st.error("Interview prep generation failed. API quota may be exceeded. Try again later.")
        else:
            st.markdown("<div style='text-align:center; padding:4rem 2rem;'><div style='font-size:3rem;'>🎤</div><div style='color:#505080;'>Upload your resume and paste a JD to get role-specific interview questions.</div></div>", unsafe_allow_html=True)
