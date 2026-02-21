import google.generativeai as genai
import os

# Configure API Key
# You can set this as an environment variable: GEMINI_API_KEY
api_key = "AIzaSyArEmc_VIHkVxRLdtVu_MAsmGBXKi5QGDk"
if not api_key:
    api_key = input("Enter your Gemini API key: ")

genai.configure(api_key=api_key)

# Initialize Gemini 2.5 Flash model
model = genai.GenerativeModel("gemini-2.5-flash")

print("=" * 50)
print("     🤖 AI DAY PLANNER with GEMINI API 🤖")
print("=" * 50)
print("\nWelcome! I'm your AI Day Planner assistant.")
print("Tell me about your preferences and I'll create a personalized day plan for you.")
print("Type 'quit' to exit.\n")

# Initialize chat for conversation
chat = model.start_chat(history=[])

# System instruction for the model
system_prompt = """You are an enthusiastic and helpful AI Day Planner assistant. Your role is to:
1. Ask the user about their current mood, budget, and location preferences
2. Understand their goals and available time
3. Create detailed, personalized day plans with activities for morning, afternoon, and evening
4. Provide motivation and productivity tips
5. Be conversational and friendly
6. Ask follow-up questions to better understand their needs
7. Suggest timing and duration for each activity

When planning their day, consider:
- Their energy level and mood
- Budget constraints
- Location preferences (indoor, outdoor, city)
- Work/life balance
- Breaks and rest time
- Meal times

Format your day plan clearly with:
⏵ Morning (6 AM - 12 PM)
⏵ Afternoon (12 PM - 6 PM)
⏵ Evening (6 PM - 11 PM)

Include specific times and durations for activities. Be creative and inspiring!"""

# Initial message from assistant
initial_response = chat.send_message(
    f"{system_prompt}\n\nStart the conversation by warmly greeting the user and asking about their mood, budget, and what kind of day they want to plan. Keep it conversational!"
)
print(f"Assistant: {initial_response.text}\n")

# Chat loop
while True:
    user_input = input("You: ").strip()
    
    if user_input.lower() in ['quit', 'exit', 'bye']:
        print("\nAssistant: Goodbye! Have an amazing day! 🌟")
        break
    
    if not user_input:
        continue
    
    # Send user message and get response
    try:
        response = chat.send_message(user_input)
        print(f"\nAssistant: {response.text}\n")
    except Exception as e:
        print(f"Error: {e}")
        print("Please check your API key and try again.\n")
