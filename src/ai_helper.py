"""
ApplyMate AI - AI Helper
=========================
Supports both Groq (default, free, no user key needed)
and Gemini (optional, user's own key).
"""

import streamlit as st


def ask_groq(prompt: str, max_tokens: int = 2000) -> str:
    """Use Groq API (server key, free for all users)."""
    try:
        from groq import Groq
        api_key = st.secrets["GROQ_API_KEY"]
        client = Groq(api_key=api_key)
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"AI request failed: {str(e)}")
        return None


def ask_gemini(prompt: str, api_key: str, max_tokens: int = 2000) -> str:
    """Use Gemini API (user's own key)."""
    try:
        import google.generativeai as genai
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"Gemini request failed: {str(e)}")
        return None
