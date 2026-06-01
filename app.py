"""
ApplyMate AI - Main Application Entry Point
==========================================
Open Source Hackathon 2025 | Elite Coders
Author: Dnyaneshwar Gumalwad
"""

import streamlit as st

# ─── Page Config ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="ApplyMate AI",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── Header ─────────────────────────────────────────────────────────────────
st.title("🎯 ApplyMate AI")
st.markdown(
    "**The only open-source, end-to-end AI job application assistant.**  \n"
    "Paste a JD + Resume → Get ATS Score, Cover Letter, Skill Gap & Interview Prep — All Free."
)
st.divider()

# ─── Sidebar Navigation ─────────────────────────────────────────────────────
st.sidebar.title("🧭 Navigation")
page = st.sidebar.radio(
    "Choose a module:",
    [
        "🏠 Home",
        "📊 ATS Score Analyzer",
        "🔑 Keyword Gap Analysis",
        "✍️ Cover Letter Generator",
        "📈 Skill Gap Roadmap",
        "🎤 Interview Prep",
    ]
)

st.sidebar.divider()
st.sidebar.markdown("### 📌 How to Use")
st.sidebar.markdown(
    "1. Upload your **Resume (PDF)**\n"
    "2. Paste the **Job Description**\n"
    "3. Run each module\n"
    "4. Apply with confidence! 🚀"
)

# ─── Pages ──────────────────────────────────────────────────────────────────
if page == "🏠 Home":
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("### 📊 ATS Score\nKnow your resume score before applying")
    with col2:
        st.success("### ✍️ Cover Letter\nAI-generated, tailored to each JD")
    with col3:
        st.warning("### 🎤 Interview Prep\nRole-specific Q&A to ace your interview")

    st.markdown("---")
    st.markdown(
        "#### 👈 Select a module from the sidebar to get started!\n\n"
        "> **Built for the Open Source Hackathon 2025 by Elite Coders**  \n"
        "> Fully open source · No account needed · No data stored"
    )

elif page == "📊 ATS Score Analyzer":
    st.header("📊 ATS Score Analyzer")
    st.info("🚧 Coming in Day 2 — ATS scoring engine being built!")

elif page == "🔑 Keyword Gap Analysis":
    st.header("🔑 Keyword Gap Analysis")
    st.info("🚧 Coming in Day 3 — Keyword analyzer being built!")

elif page == "✍️ Cover Letter Generator":
    st.header("✍️ Cover Letter Generator")
    st.info("🚧 Coming in Day 4 — Cover letter generator being built!")

elif page == "📈 Skill Gap Roadmap":
    st.header("📈 Skill Gap Roadmap")
    st.info("🚧 Coming in Day 5 — Skill roadmap engine being built!")

elif page == "🎤 Interview Prep":
    st.header("🎤 Interview Prep")
    st.info("🚧 Coming in Day 5 — Interview Q&A generator being built!")
