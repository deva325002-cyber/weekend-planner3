from flask import Flask, render_template, request, jsonify
from groq import Groq
import os

# Get the directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, 
            template_folder=os.path.join(BASE_DIR, 'templates'),
            static_folder=os.path.join(BASE_DIR, 'static'))

# Configure Groq API Key
# Get your key from https://console.groq.com/keys
# Set via environment variable: export GROQ_API_KEY=your_key_here
api_key = os.environ.get("GROQ_API_KEY", "YOUR_GROQ_API_KEY_HERE")

client = Groq(api_key=api_key)

# Valid Groq model — use llama3-70b or llama-3.1-70b-versatile
MODEL = "llama-3.1-70b-versatile"

# Store chat sessions in memory
chat_sessions = {}

system_prompt = """You are an enthusiastic and helpful AI Weekend Planner assistant named Genie.

CRITICAL RULE: Ask ONLY ONE question per message. NEVER ask two questions in one message.

Gather information in this exact order, one question at a time:
1. Energy level — Options: low, medium, high (or custom)
2. Budget — Options: low, medium, high (or custom)
3. Which time of day to spend the budget — Options: morning, afternoon, evening
4. Activity interests — Options: outdoor, dining, entertainment, shopping
5. Who they're spending the weekend with — Options: solo, friends, family, partner

After collecting all 5 answers, generate a detailed weekend plan with:
- Morning section
- Afternoon section  
- Evening section

Format activities clearly with bold names like:
• **Activity Name** - brief description

For the time of day they chose for their budget, suggest activities matching their budget level.
For other times, suggest free or very low-cost activities.

Rules:
- One question per message, always
- Wait for the user to answer before asking the next question
- Be warm, encouraging, and conversational
- Keep suggestions specific and inspiring
- Do not include prices or exact times unless asked"""


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/start-chat', methods=['POST'])
def start_chat():
    """Initialize a new chat session and return the first message."""
    data = request.get_json() or {}
    session_id = data.get('session_id', 'default')

    chat_sessions[session_id] = []

    messages = [
        {"role": "system", "content": system_prompt},
        {
            "role": "user",
            "content": (
                "Greet the user warmly with a short intro (1-2 sentences). "
                "Then ask ONLY about their energy level for the weekend with options: low, medium, high, or custom."
            )
        }
    ]

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0.75,
            max_tokens=512
        )
        initial_message = response.choices[0].message.content

        chat_sessions[session_id] = [
            {"role": "system", "content": system_prompt},
            {"role": "assistant", "content": initial_message}
        ]

        return jsonify({'message': initial_message, 'session_id': session_id})

    except Exception as e:
        print(f"[ERROR] start_chat: {e}")
        return jsonify({'error': f'Error starting chat: {str(e)}'}), 500


@app.route('/api/send-message', methods=['POST'])
def send_message():
    """Receive a user message and return the assistant response."""
    data = request.get_json() or {}
    user_message = data.get('message', '').strip()
    session_id = data.get('session_id', 'default')

    if not user_message:
        return jsonify({'error': 'Empty message'}), 400

    # Restore or create session
    if session_id not in chat_sessions:
        chat_sessions[session_id] = [{"role": "system", "content": system_prompt}]

    messages = chat_sessions[session_id].copy()
    messages.append({"role": "user", "content": user_message})

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0.75,
            max_tokens=1024
        )
        assistant_message = response.choices[0].message.content

        # Save updated history
        chat_sessions[session_id].append({"role": "user", "content": user_message})
        chat_sessions[session_id].append({"role": "assistant", "content": assistant_message})

        return jsonify({'message': assistant_message, 'session_id': session_id})

    except Exception as e:
        print(f"[ERROR] send_message: {e}")
        return jsonify({'error': f'Error: {str(e)}'}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)