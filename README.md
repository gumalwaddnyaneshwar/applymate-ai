# 🎯 ApplyMate AI

<div align="center">

![ApplyMate AI Banner](assets/banner.png)

**The only open-source, end-to-end AI job application assistant.**  
Paste a Job Description + Resume → Get ATS Score, Keyword Fixes, Cover Letter, Skill Gap Roadmap & Interview Questions. All free. No account. No data stored.

[![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red?style=for-the-badge&logo=streamlit)](https://streamlit.io)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-Transformers-yellow?style=for-the-badge&logo=huggingface)](https://huggingface.co)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Open Source](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-red?style=for-the-badge)](https://github.com)
[![OSH 2025](https://img.shields.io/badge/OSH-Elite%20Coders%202025-purple?style=for-the-badge)](https://oshack.xyz)

[🚀 Live Demo](#) · [📖 Docs](#installation) · [🤝 Contribute](#contributing) · [🐛 Report Bug](issues)

</div>

---

## ❓ Why ApplyMate AI?

> **"Why not just use Jobscan or Enhancv?"**

Every existing tool stops halfway. Here's what makes ApplyMate AI different:

| Feature | Jobscan | Enhancv | GitHub OSS Tools | **ApplyMate AI** |
|---------|:-------:|:-------:|:----------------:|:----------------:|
| ATS Score | ✅ | ❌ | ✅ | ✅ |
| Missing Keywords | ✅ | ❌ | ✅ | ✅ |
| Resume Rewrite Suggestions | ⚠️ Limited | ❌ | ❌ | ✅ |
| Cover Letter Generator | ❌ Paid | ❌ | ❌ | ✅ |
| Interview Q&A Generator | ❌ | ❌ | ❌ | ✅ |
| Skill Gap Roadmap | ❌ | ❌ | ❌ | ✅ |
| Indian Job Market Support | ❌ | ❌ | ❌ | ✅ |
| 100% Free Forever | ❌ | ❌ | ✅ | ✅ |
| Open Source | ❌ | ❌ | ✅ | ✅ |
| No Data Stored / Privacy First | ❌ | ❌ | ❌ | ✅ |
| No Account Required | ❌ | ❌ | ✅ | ✅ |

**ApplyMate AI is the only tool that completes the FULL application pipeline in one place — for free.**

---

## ✨ Features

### 📊 1. ATS Score Analyzer
- Paste any Job Description + upload your Resume (PDF)
- Get an instant **ATS compatibility score (0–100)**
- See exactly where you're losing points

### 🔑 2. Keyword Gap Analysis
- Detects **missing hard skills, soft skills, and role-specific keywords**
- Prioritized by importance (Critical / Important / Optional)
- Suggests natural ways to add them without keyword stuffing

### ✍️ 3. AI Cover Letter Generator
- Generates a **tailored, professional cover letter** for each JD
- Matches tone and keywords from the job description
- One-click copy or download as `.txt`

### 📈 4. Skill Gap Roadmap
- Identifies skills you're missing for the target role
- Suggests **free resources** (Coursera, YouTube, docs) to fill each gap
- Estimated time to upskill per skill

### 🎤 5. Interview Question Generator
- Generates **role-specific interview questions** based on the JD
- Includes both technical and HR/behavioral questions
- Provides model answers to help you prepare

---

## 🛠️ Tech Stack

```
ApplyMate AI
├── Frontend        → Streamlit (Python)
├── Resume Parsing  → PyPDF2 + pdfplumber
├── AI Engine       → Google Gemini API / HuggingFace Transformers
├── NLP Pipeline    → LangChain
├── Deployment      → Streamlit Cloud (Free)
└── Language        → Python 3.9+
```

---

## 🚀 Installation

### Prerequisites
- Python 3.9+
- pip
- A free [Google Gemini API Key](https://makersuite.google.com/app/apikey)

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/applymate-ai.git
cd applymate-ai

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env
# Add your Gemini API key to .env file

# 5. Run the app
streamlit run src/app.py
```

The app will open at `http://localhost:8501` 🎉

---

## 📁 Project Structure

```
applymate-ai/
├── src/
│   ├── app.py              # Main Streamlit app entry point
│   ├── ats_scorer.py       # ATS scoring engine
│   ├── keyword_analyzer.py # Keyword gap detection
│   ├── cover_letter.py     # Cover letter generator
│   ├── skill_roadmap.py    # Skill gap roadmap builder
│   ├── interview_prep.py   # Interview Q&A generator
│   └── utils.py            # Helper functions (PDF parsing, etc.)
├── sample_data/
│   ├── sample_resume.pdf   # Sample resume for testing
│   └── sample_jd.txt       # Sample job description
├── assets/
│   └── banner.png          # Project banner
├── .env.example            # Environment variable template
├── requirements.txt        # Python dependencies
├── LICENSE                 # MIT License
└── README.md               # This file
```

---

## 🗺️ Roadmap

- [x] Project setup & architecture
- [ ] Resume parser (PDF → text)
- [ ] ATS scoring engine
- [ ] Keyword gap analyzer
- [ ] Cover letter generator
- [ ] Skill gap roadmap
- [ ] Interview Q&A generator
- [ ] Streamlit UI (all modules integrated)
- [ ] Deploy to Streamlit Cloud
- [ ] Support for LinkedIn profile input
- [ ] Multi-language support (Hindi + English)
- [ ] Chrome Extension (future)

---

## 🤝 Contributing

Contributions are welcome! This project is built during the **Open Source Hackathon by Elite Coders**.

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 👨‍💻 Author

**Dnyaneshwar Gumalwad**  
BCA in AI/ML | JSPM University, Pune  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://linkedin.com/in/YOUR_PROFILE)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?logo=github)](https://github.com/YOUR_USERNAME)

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 🏆 Built For

<div align="center">
  <strong>Open Source Hackathon 2025 · Elite Coders · <a href="https://oshack.xyz">oshack.xyz</a></strong>
</div>
