# 🎯 Smart Event Management System with AI Assistant

## 📌 Overview

The **Smart Event Management System with AI Assistant** is an intelligent platform designed to streamline event planning and management. It integrates an **AI-powered assistant** to automate tasks such as event scheduling, attendee queries, and personalized recommendations.

This system enhances user experience by combining **automation, real-time interaction, and data-driven insights**.

---

## 🚀 Features

* 📅 Event creation and management
* 🤖 AI Assistant for user queries and guidance
* 🔍 Smart search and filtering of events
* 🧾 Attendee registration and tracking
* 📊 Real-time event insights and updates
* 💬 Interactive chatbot for event-related questions

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit 
* **Backend:** FastAPI
* **Database:** SQLite / PostgreSQL
* **AI/ML:** NLP, LLM (for assistant)
* **Libraries:** LangChain 

---

## 📂 Project Structure
## 📂 Project Structure

```bash
Smart_Event_Management_System/
│
├── backend/                      # FastAPI backend services
│   ├── __pycache__/              # Python cache files
│   ├── database/                 # Database configuration & connections
│   ├── models/                   # Data models and schemas
│   ├── routes/                   # API endpoints
│   ├── services/                 # Business logic and processing
│   ├── credentials.json          # API credentials/config (keep secure)
│   ├── events.db                 # SQLite database
│   ├── main.py                   # FastAPI entry point
│   ├── sheets.py                 # Integration with Google Sheets
│   ├── requirements.txt          # Backend dependencies
│   └── Dockerfile                # Backend container setup
│
├── frontend/                     # User interface (Streamlit apps)
│   ├── __pycache__/              # Python cache files
│   ├── admin_dashboard.py        # Admin panel for event management
│   ├── student_app.py            # User interface for participants
│   ├── requirements.txt          # Frontend dependencies
│   └── Dockerfile                # Frontend container setup
│
├── .env                          # Environment variables
├── .env.example                  # Sample environment config
├── .gitignore                    # Git ignore rules
├── docker-compose.yml            # Multi-container orchestration
└── README.md                     # Project documentation
```

```

---

## ⚙️ Installation

```bash id="h4m2qv"
git clone https://github.com/your-username/smart-event-management.git
cd smart-event-management
pip install -r requirements.txt
```

---

## ▶️ How to Run

### 1️⃣ Start Backend

```bash id="z2g9mx"
uvicorn main:app --reload
```

### 2️⃣ Start Frontend

```bash id="l0k3sd"
streamlit run app.py
```

---

## 🤖 AI Assistant Capabilities

* Answers event-related queries
* Provides schedule recommendations
* Assists with event navigation
* Handles FAQs automatically
* Supports conversational interaction

---

## 🧪 Example Use Case

1. User registers for an event
2. AI assistant suggests sessions based on interest
3. User asks questions → chatbot responds instantly
4. System tracks participation and engagement

---

## 📸 Screenshots

### 🏠 Home Page



### 🤖 AI Assistant Chat



### 📊 Dashboard



---

## 💡 Use Cases

* 🎓 College event management
* 🏢 Corporate event planning
* 🎤 Conferences and seminars
* 🎉 Community events

---


## 👩‍💻 Author

**Maha Vigneshwari**
Generative AI Developer

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
