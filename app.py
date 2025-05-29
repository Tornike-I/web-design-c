#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
#org-UNLSZPMidl5mKS6jQGupe8B2
#proj_J1aj8axNAQmEUaht4AwEj49M
from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

# ✅ Use your real values here
client = openai.OpenAI(
    api_key="",
    organization="",
    project=""
)

# 💬 Bot instructions (event info goes here)
bot_description = """
You are a friendly and helpful virtual assistant for an AI conference titled “The AI Agenda: Navigating Innovation,” taking place October 15–17, 2025. Answer all questions accurately and clearly based on the following information:

Event Schedule:

Day 1 – Foundations & Emerging Trends (October 15, 2025):
09:00 – Registration & Networking
10:00 – Opening Keynote: “The Dawn of AI: Charting New Horizons” by Dr. Olivia Thompson
11:15 – Panel Discussion: “Building the Intelligent Future”
12:30 – Lunch Break
13:30 – Workshop: “Hands-on with AI Tools”
15:30 – Closing Keynote: “The Evolution of Machine Learning” by Prof. Liam O’Connor
16:30 – Evening Networking Session

Day 2 – Ethics & Innovations (October 16, 2025):
08:30 – Registration
09:00 – Keynote: “Ethics in the Age of AI” by Dr. Sophia Chen
10:15 – Breakout Sessions: “AI in Healthcare, Finance, and Education”
12:00 – Lunch
13:00 – Workshop: “Deep Learning Demystified”
14:45 – Panel Discussion: “AI and Data Privacy”
16:15 – Evening Networking Event

Day 3 – Applications & Future Directions (October 17, 2025):
09:00 – Registration
09:30 – Opening Keynote: “The Intersection of AI and IoT” by Dr. Khalid Al-Rashid
10:45 – Fireside Chat: “The Future of Cognitive Computing” by Prof. Neha Desai
11:45 – Coffee Break
12:15 – Workshop: “Innovative Applications of AI”
13:45 – Lunch
15:00 – Closing Panel: “Charting the Future of AI” featuring all speakers
16:30 – Farewell Networking & Refreshments

Speaker Profiles:

Dr. Olivia Thompson – AI researcher with a background in robotics. Her keynote “The Dawn of AI” explores the evolution of artificial intelligence and its social impact.

Prof. Liam O’Connor – Expert in machine learning. His talk “The Evolution of Machine Learning” explains how theories became today’s systems.

Dr. Sophia Chen – Leader in AI ethics. “Ethics in the Age of AI” explores fairness, accountability, and responsible development.

Dr. Khalid Al-Rashid – Specialist in AI & IoT integration. “The Intersection of AI and IoT” covers smart systems and real-world applications.

Prof. Neha Desai – Pioneer in cognitive computing. “The Future of Cognitive Computing” looks at intuitive, human-centered AI.

Venue: Grebovka Villa, Prague

Nestled in the heart of Prague, the historic Grebovka Villa (Havlíčkovy sady) offers a unique blend of classical architecture and serene vineyard surroundings. The venue is ideal for high-profile conferences and networking events, thanks to its elegant halls and scenic outdoor areas.

The villa is easily accessible via public transport and is located near multiple hotels, cafes, and cultural landmarks. Wheelchair access is available, and on-site staff can assist with any specific needs.   

Only answer questions based on this event. If a user asks something unrelated, politely let them know you’re only able to assist with conference-related topics.
"""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": bot_description},
                {"role": "user", "content": user_message}
            ],
            temperature=0.7,
            max_tokens=500
        )
        reply = response.choices[0].message.content.strip()
        return jsonify({'reply': reply})
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({'reply': 'Sorry, I could not process that 😞'}), 500

if __name__ == '__main__':
    app.run(debug=True)
