# 🎯 ApplyMate AI

<div align="center">

### **The only open-source, end-to-end AI job application assistant.**

[![Live Demo](https://img.shields.io/badge/🚀%20Live%20Demo-applymate--ai.streamlit.app-6C63FF?style=for-the-badge)](https://applymate-ai.streamlit.app)
[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red?style=for-the-badge&logo=streamlit)](https://streamlit.io)
[![Gemini AI](https://img.shields.io/badge/Gemini-AI%20Powered-orange?style=for-the-badge&logo=google)](https://aistudio.google.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![OSH 2026](https://img.shields.io/badge/OSH-Elite%20Coders%202026-purple?style=for-the-badge)](https://oshack.xyz)

**Paste a Job Description + Resume → Get ATS Score, Keyword Fixes, Cover Letter, Skill Gap Roadmap & Interview Questions.**
**All free. No account. No data stored.**

[🚀 Try Live App](https://applymate-ai.streamlit.app) · [⭐ Star this Repo](https://github.com/gumalwaddnyaneshwar/applymate-ai) · [🐛 Report Bug](https://github.com/gumalwaddnyaneshwar/applymate-ai/issues) · [💡 Request Feature](https://github.com/gumalwaddnyaneshwar/applymate-ai/issues)

</div>

---

## ❓ Why ApplyMate AI?

> **"Why not just use Jobscan or Enhancv?"**

Every existing tool stops halfway. ApplyMate AI completes the **entire application pipeline** in one place — for free.

| Feature | Jobscan | Enhancv | Others | **ApplyMate AI** |
|---------|:-------:|:-------:|:------:|:----------------:|
| ATS Score | ✅ | ❌ | ✅ | ✅ |
| AI Keyword Analysis | ❌ | ❌ | ❌ | ✅ |
| Cover Letter Generator | ❌ Paid | ❌ | ❌ | ✅ |
| Interview Q&A Generator | ❌ | ❌ | ❌ | ✅ |
| Skill Gap Roadmap | ❌ | ❌ | ❌ | ✅ |
| Indian Job Market Support | ❌ | ❌ | ❌ | ✅ |
| 100% Free Forever | ❌ | ❌ | ❌ | ✅ |
| Open Source | ❌ | ❌ | ❌ | ✅ |
| No Data Stored | ❌ | ❌ | ❌ | ✅ |
| No Account Required | ❌ | ❌ | ✅ | ✅ |

---

## ✨ Features

### 📊 1. ATS Score Analyzer
- Upload resume (PDF) + paste any Job Description
- Get instant **ATS compatibility score (0–100)**
- See exactly where you're losing points
- Works without any API key

### 🔑 2. AI Keyword Gap Analyzer *(Gemini Powered)*
- **Smarter than basic keyword matching** — understands context
- Detects missing Critical / Important / Optional keywords
- Gives specific suggestions for each missing keyword
- Shows category (Programming, AI/ML, DevOps, Soft Skills, etc.)

### ✍️ 3. AI Cover Letter Generator *(Gemini Powered)*
- Generates a **tailored, professional cover letter** for each JD
- Matches tone and keywords from the job description
- Includes email subject line + key strengths highlighted
- One-click copy to clipboard

### 📈 4. Skill Gap Roadmap *(Gemini Powered)*
- Identifies your **job readiness score** (%)
- Lists skills you have vs skills you need
- Provides **free learning resources** for each gap (YouTube, docs, courses)
- Week-by-week action plan to become interview-ready

### 🎤 5. Interview Prep *(Gemini Powered)*
- Generates **role-specific technical questions** based on the JD
- HR/behavioral questions with model answers
- Project-based questions tailored to your resume
- Quick interview tips for the specific role

---

## 🛠️ Tech Stack

```
ApplyMate AI
├── Frontend        → Streamlit (Python)
├── Resume Parsing  → PyPDF2 + pdfplumber
├── AI Engine       → Google Gemini 2.0 Flash API
├── NLP Pipeline    → NLTK + Scikit-learn
├── Deployment      → Streamlit Cloud (Free)
└── Language        → Python 3.10+
```

---

## 🚀 Quick Start

### Option 1: Use the Live App (Recommended)
👉 **[applymate-ai.streamlit.app](https://applymate-ai.streamlit.app)**

No installation needed!

### Option 2: Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/gumalwaddnyaneshwar/applymate-ai.git
cd applymate-ai

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set up environment variables
cp .env.example .env
# Add your Gemini API key to .env

# 4. Run the app
streamlit run src/app.py
```

Get your free Gemini API key at: **[aistudio.google.com](https://aistudio.google.com)**

---

## 📁 Project Structure

```
applymate-ai/
├── src/
│   ├── app.py              # Main Streamlit app (all 5 modules)
│   ├── ats_scorer.py       # ATS scoring engine (no API needed)
│   ├── keyword_analyzer.py # AI keyword gap analyzer (Gemini)
│   ├── cover_letter.py     # AI cover letter generator (Gemini)
│   ├── skill_roadmap.py    # AI skill roadmap builder (Gemini)
│   ├── interview_prep.py   # AI interview Q&A generator (Gemini)
│   └── utils.py            # PDF parsing helpers
├── .streamlit/
│   └── config.toml         # Streamlit theme config
├── sample_data/
│   └── sample_jd.txt       # Sample job description for testing
├── .env.example            # Environment variable template
├── requirements.txt        # Python dependencies
├── LICENSE                 # MIT License
└── README.md               # This file
```

---

## 🗺️ Roadmap

- [x] ATS Score Analyzer
- [x] AI Keyword Gap Analyzer
- [x] AI Cover Letter Generator
- [x] AI Skill Gap Roadmap
- [x] AI Interview Prep
- [x] Deploy to Streamlit Cloud
- [ ] User brings own API key (no quota limits)
- [ ] LinkedIn profile input support
- [ ] Multi-language support (Hindi + English)
- [ ] Resume rewrite suggestions
- [ ] Chrome Extension

---

## 🤝 Contributing

Contributions are welcome! This project was built during the **Open Source Hackathon 2026 by Elite Coders**.

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 👨‍💻 Author

**Dnyaneshwar Gumalwad**
BCA in AI/ML | JSPM University, Pune

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)](https://linkedin.com/in/gumalwaddnyaneshwar)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=flat&logo=github)](https://github.com/gumalwaddnyaneshwar)
[![Research Paper](https://img.shields.io/badge/Research-IJARSCT%202026-green?style=flat)](https://ijarsct.co.in/Paper35343.pdf)

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

### 🏆 Built for Open Source Hackathon 2026 · Elite Coders · [oshack.xyz](https://oshack.xyz)

**If this helped you, please ⭐ star the repo!**

</div>
