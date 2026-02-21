# 🤖 AI Day Planner Website

A Flask-based web application for your AI Day Planner using the Gemini API.

## 📋 Project Structure

```
weekend-planner/
├── app.py                 # Flask application
├── main.py               # Original CLI version
├── requirements.txt      # Python dependencies
├── templates/
│   └── index.html       # Chat interface HTML
└── static/
    └── style.css        # Styling
```

## 🚀 Getting Started

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Flask App

```bash
python app.py
```

The application will start on `http://localhost:5000`

### 3. Open in Browser

Open your web browser and navigate to:
```
http://localhost:5000
```

## ✨ Features

- 💬 Real-time chat interface with the AI Day Planner
- 🎨 Modern, responsive UI design
- 📱 Works on desktop and mobile devices
- ⏰ Personalized day planning
- 🎯 Budget and preference consideration
- 🌅 Morning, afternoon, and evening planning

## 🎯 How to Use

1. Start a conversation with the AI Day Planner
2. Tell it about your mood, budget, and preferences
3. Get a personalized day plan with specific times and activities
4. Ask follow-up questions to refine your plan
5. Type "quit" to end the conversation

## ⚙️ Configuration

The API key is already set in `app.py`. If you want to use a different key:

1. Open `app.py`
2. Replace the `api_key` variable with your Gemini API key
3. Or set the environment variable `GEMINI_API_KEY`

## 🔧 Troubleshooting

- **Port already in use**: Change the port in `app.py` (line: `app.run(debug=True, port=5000)`)
- **API Key issues**: Verify your Gemini API key is valid
- **Connection errors**: Check your internet connection

## 📝 Notes

- The original CLI version is available in `main.py`
- Each browser session has its own independent chat history
- Messages are not persisted between page reloads

---

Enjoy your personalized day planning with AI! 🌟
