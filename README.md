College Event Registration & Management System

A full-stack event management platform that allows students to register for college events and receive automated confirmations.
Built using FastAPI, Streamlit, SQLite

This system simulates a real institutional event platform with registration, admin dashboard, chat assistant, email notifications, and optional RAG support.

🚀 Features:
👩‍🎓 Student Features:
Register for events
View available events
Real-time confirmation
Chat support system
QR code generation for entry
Email confirmation

🛠 Admin Features:
Create/manage events
View registrations
Monitor participants
Admin dashboard
Export or sync data (Sheets integration)

🤖 AI / Smart Features:
Chat assistant system
Retrieval-based responses (RAG module)
Rule-based automation
Email automation
Google Sheets sync

🧠 System Architecture:

Student UI → FastAPI Backend → Services Layer → Database
↘ Chat/RAG
↘ Email
↘ Sheets

🛠 Tech Stack:
Backend:
FastAPI
Python
SQLAlchemy
SQLite

Frontend:
Streamlit
AI / Automation
RAG module
Rule-based chat
Email automation
Integrations
Google Sheets API
QR generation
SMTP Email

📁 Project Structure:
college-event-registration-system/
│
├── backend/
│   │
│   ├── main.py
│   ├── requirements.txt
│   ├── events.db
│   ├── credentials.json
│   ├── rules.txt
│   ├── string_qr.png
│   └── sheets.py
│
│   ├── database/
│   │   ├── db.py
│   │   └── deps.py
│   │
│   ├── models/
│   │   ├── tables.py
│   │   └── pydantic.py
│   │
│   ├── routes/
│   │   └── routes.py
│   │
│   └── services/
│       ├── auth.py
│       ├── data.py
│       ├── email_service.py
│       └── rag.py
│
├── frontend/
│   ├── student_app.py
│   ├── admin_dashboard.py
│   └── requirements.txt
│
├── .env.example
├── .gitignore
└── README.md

⚙️ Setup Instructions:

1️⃣ Clone Repository
git clone https://github.com/YOUR_USERNAME/college-event-registration.git
cd college-event-registration

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install fastapi uvicorn streamlit sqlalchemy pydantic requests

▶️ Run Backend:
cd backend
uvicorn main:app --reload

Backend URL:

http://localhost:8000

Swagger Docs:

http://localhost:8000/docs

▶️ Run Frontend:

Open new terminal:

cd frontend
streamlit run app.py

Frontend URL:

http://localhost:8501

📡 API Endpoints
Get all events:
GET /events

Add new event:
POST /events

Register student:
POST /register

Login:
POST/login

🧠 How it Works:

Student opens Streamlit app
Fetches events from FastAPI
Student fills registration form
Data sent to FastAPI backend
Stored in SQLite database
Admin can view all registrations

📊 Dataset

This project does not use external datasets.
All data is generated internally.

Includes:
Student registration data
Event details
Chat messages
Admin activity
Stored in SQLite for demo purposes.

🔒 Ethics & Privacy:
Built for educational use
Stores only basic user data
No third-party data sharing
Chat data stored locally
Avoid entering sensitive data
Can be extended with encryption & auth

Focus:
Responsible data handling
Transparency
Privacy awareness
