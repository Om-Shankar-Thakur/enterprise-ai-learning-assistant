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
```
Response format:
```
{
  "answer": "...",
  "confidence": "high",
  "related_topics": [],
  "suggested_next_action": ""
}
```

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

## Follow these steps-
1. Create Virtual Environment
```
python -m venv venv
```
2. Activate virtual environment
```
venv\Scripts\activate
```
3. Upgarde pip
```
python -m pip install --upgrade pip
```
4. Install requirements
```
pip install -r requirements.txt
```
5. Start FAstAPI
```
uvicorn app.main:app --reload
```
6. Navigate to this page and check
```
http://127.0.0.1:8000/docs
```
---


