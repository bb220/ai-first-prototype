# 🧪 AI-first application prototype

An AI-first application prototype with a conversational interface. This project includes a modern full-stack architecture with:

- **Agent**: LangChain agent with callable example tools (e.g., `get_balance`)
- **Backend**: FastAPI API endpoint 
- **Frontend**: Next.js (React) chat UI   

---

## 🧱 Project Structure

```
finance-copilot/
├── backend/         # FastAPI server with LangChain agent
│   └── main.py
├── frontend/        # Next.js 13+ frontend UI
│   └── app/page.tsx
├── agent/           # Isolated LangChain agent logic
│   └── agent_runner.py
├── .env             # OPENAI_API_KEY here
├── requirements.txt
└── README.md
```

---

## 🚀 Features

- 🔁 Conversational chat UI  
- 🧠 LangChain-powered reasoning  
- 🔌 Tool support (`get_balance(user_id)`)  
- 🌐 Frontend and backend are decoupled but work together 

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourname/finance-copilot.git
cd finance-copilot
```

### 2. Add your OpenAI API key

Create a `.env` file in the root of the project:

```
OPENAI_API_KEY=your-openai-key-here
```

---

## 🖥 Backend (FastAPI)

### 1. Set up Python environment

```bash
cd backend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r ../requirements.txt
```

### 3. Run the FastAPI server

```bash
uvicorn main:app --reload
```

API will be available at: `http://localhost:8000/chat`

---

## 🌐 Frontend (Next.js)

### 1. Install dependencies

```bash
cd ../frontend
npm install
```

### 2. Run the development server

```bash
npm run dev
```

Visit: [http://localhost:3000](http://localhost:3000)

---

## 🧠 Agent Logic

LangChain agent lives in:

```
/agent/agent_runner.py
```

Example tool:

```python
def get_balance(user_id: str) -> str:
    return f"User {user_id} has a balance of $1,234.56"
```

You can register more tools easily by adding them to the `tools` list and exposing them to the agent.

---

## 🧪 Example Interaction

1. Go to [http://localhost:3000](http://localhost:3000)  
2. Ask something like:

```
What is my balance?
```

The system will:
- Send the request to FastAPI  
- Route it to the LangChain agent  
- Run the appropriate tool  
- Return the result in the frontend  

---

## 📝 License

MIT License

