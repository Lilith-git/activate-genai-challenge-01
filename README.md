# 🚀 GenTech AI - Challenge 01: Azure OpenAI Foundation Setup

Welcome to Challenge 01 of the **Activate GenAI Hackathon**! This project sets up a production-grade **Azure OpenAI foundation**, with working FastAPI endpoints and robust dev tooling to support further RAG development.

---

## 🧠 Overview

This repo enables a complete LLM backend built with:

- **Azure OpenAI** (`gpt-35-turbo`, `text-embedding-ada-002`)
- **Python 3.12** with `FastAPI`
- **Environment secrets** managed via `.env`
- **/ask** and **/embed** endpoints ready for RAG integration

---

## ⚙️ Tech Stack

| Component         | Details                                |
|------------------|----------------------------------------|
| Backend API      | FastAPI + Uvicorn                      |
| LLM Provider     | Azure OpenAI                           |
| Embedding Model  | text-embedding-ada-002                 |
| Dev Tooling      | python-dotenv, model_tester.py         |

---

## 🖥️ One-Click Setup (Windows PowerShell)

Paste the following into **PowerShell** to set up your environment in seconds:

```powershell
# 🧪 Step 0: Move to project directory
cd "C:\Users\demouser\Desktop\Hackathon_Lilith_Karri\Challenge 1"

# 🐍 Step 1: Create virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate

# 📦 Step 2: Install dependencies
pip install --upgrade pip
pip install fastapi uvicorn openai python-dotenv

# 🧪 Step 3: Test your OpenAI credentials
python model_tester.py

# 🚀 Step 4: Launch the FastAPI app
uvicorn gentech_ai:app --reload --port 8000
