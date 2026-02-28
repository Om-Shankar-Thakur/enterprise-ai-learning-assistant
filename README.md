# AI Learning Mentor

An LLM-powered AI Learning Assistant built using FastAPI and Groq.

This system acts as an intelligent mentor inside a corporate-style training platform. It provides domain-aware guidance, structured responses, and learning recommendations similar to enterprise LMS platforms.

---

## 🚀 Features

- Personalized greeting for learners
- Domain-aware responses
- Structured JSON output
- Groq LLM integration (LLaMA 3.3 70B)
- FastAPI backend
- Adaptive learning guidance
- Interview preparation support
- Mock interview suggestion system

---

## 🏗 Tech Stack

- Python
- FastAPI
- Groq API
- Uvicorn
- Pydantic

---

## 📂 Project Structure

chatbot/
│
├── app/
│ ├── main.py
│ ├── llm_service.py
│ ├── prompt_template.py
│ ├── models.py
│ ├── validators.py
│
├── requirements.txt
├── .gitignore
├── README.md


---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

git clone https://github.com/YOUR_USERNAME/ai-learning-mentor.git
cd ai-learning-mentor


### 2️⃣ Create Virtual Environment

python -m venv venv
venv\Scripts\activate


### 3️⃣ Install Dependencies

pip install -r requirements.txt


### 4️⃣ Create .env File

Create a `.env` file in the root directory and add:

GROQ_API_KEY=your_api_key_here


### 5️⃣ Run the Server

uvicorn app.main:app --reload


Open:
http://127.0.0.1:8000/docs


---

## 🎯 API Endpoint

### POST `/chat`

Request body:

```json
{
  "domain": "GenAI",
  "message": "Explain transformers",
  "learner_name": "Om"
}
Response format:

{
  "answer": "...",
  "confidence": "high",
  "related_topics": [],
  "suggested_next_action": ""
}
🧠 Future Enhancements
XP & Mastery tracking

RAG-based learning recommendations

Mock interview mode (voice/video)

Dashboard analytics integration

Docker deployment

Frontend integration

📌 Author
Om Shankar Thakur
AI/ML Developer


---

# 🚀 After Creating README

Run:

git add README.md
git commit -m "docs: add project README with setup instructions"


Then push:

git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/ai-learning-mentor.git
git push -u origin main


---

If you want, I can now help you:

- Make this deployable on Render
- Add Docker
- Add badge + professional GitHub polish
- Or upgrade it into full RAG LMS architecture

You’re building something strong here 💪
