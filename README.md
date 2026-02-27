# TalentScout Hiring Assistant

## 📌 Project Overview
TalentScout Hiring Assistant is an AI-powered chatbot designed to conduct initial candidate screening for technical roles.

It gathers candidate information and generates customized technical interview questions based on the candidate's declared tech stack.

---

## 🛠 Tech Stack
- Python
- Streamlit
- OpenAI GPT-4
- Session State for context management

---

## ⚙ Installation

1. Clone repository
2. Install dependencies:
   pip install -r requirements.txt
3. Set OpenAI API key:
   export OPENAI_API_KEY=your_key
4. Run:
   streamlit run app.py

---

## 💡 Features
- Candidate information collection
- Dynamic technical question generation
- Context-aware conversation
- Exit handling
- Fallback mechanism
- GDPR-friendly simulated data handling

---

## 🧠 Prompt Engineering Strategy
- System prompt controls conversation scope
- Structured question generation prompt
- Clear instructions prevent deviation
- Context preserved using session state

---

## 🔐 Data Privacy
- No real database storage
- No persistent storage of sensitive data
- Uses session-based memory only

---

## 🚀 Future Improvements
- Multilingual support
- Sentiment analysis
- Cloud deployment