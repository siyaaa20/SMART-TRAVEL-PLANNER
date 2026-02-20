from flask import Flask, render_template, request
from groq import Groq
import markdown
import os
from markupsafe import Markup
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configure Groq API
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY environment variable not set")
groq_client = Groq(api_key=GROQ_API_KEY)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/generate', methods=['POST'])
def generate():
    destination = request.form['destination']
    days = int(request.form['days'])
    budget = int(request.form['budget'])
    trip_type = request.form.get('trip_type', 'solo')

    stay = budget * 0.4
    food = budget * 0.25
    travel = budget * 0.2

    # Customize prompt based on trip type
    trip_context = {
        'solo': 'a solo traveler looking for independent activities, self-discovery, and flexibility',
        'family': 'a family with kids, focusing on family-friendly activities, safety, and entertainment for all ages',
        'couple': 'a couple looking for romantic experiences, restaurants, and activities suitable for two',
        'group': 'a group of friends looking for fun group activities, social experiences, and group-friendly venues'
    }
    
    context = trip_context.get(trip_type, trip_context['solo'])

    # Generate AI itinerary using Groq (mixtral-8x7b-32768)
    try:
        prompt = f"""Create a detailed {days}-day travel itinerary for {destination} with a budget of ${budget}.

This is a {trip_type} trip for {context}.
        
Budget breakdown:
- Accommodation: ${stay}
- Food: ${food}
- Travel/Activities: ${travel}

Please provide a day-by-day itinerary with:
- Specific activities suitable for {trip_type} travel
- Restaurant recommendations (matching the trip type)
- Cost estimates for each day
- Practical tips for {trip_type} travelers in {destination}

Make it engaging and practical."""
        
        chat_completion = groq_client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama-3.3-70b-versatile",
        )
        
        itinerary_text = chat_completion.choices[0].message.content
        itinerary_html = Markup(markdown.markdown(itinerary_text))
    except Exception as e:
        itinerary_html = f"Error generating itinerary: {str(e)}"

    return render_template("result.html",
                           destination=destination,
                           trip_type=trip_type,
                           itinerary=itinerary_html,
                           stay=stay,
                           food=food,
                           travel=travel)

if __name__ == "__main__":
    app.run(debug=True)             

