from flask import Flask, render_template, request
from groq import Groq
import markdown
import os
from markupsafe import Markup
from dotenv import load_dotenv

# Load environment variables (works locally)
load_dotenv()

app = Flask(__name__)

# Configure Groq API safely
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
groq_client = Groq(api_key=GROQ_API_KEY) if GROQ_API_KEY else None


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/combined')
def combined():
    return render_template("combined.html")


@app.route('/generate', methods=['POST'])
def generate():
    # If API key is missing, prevent crash
    if not groq_client:
        return "Server configuration error: GROQ_API_KEY not set."

    try:
        destination = request.form.get('destination', '')
        days = int(request.form.get('days', 1))
        budget = int(request.form.get('budget', 1000))
        trip_type = request.form.get('trip_type', 'solo')

        stay = round(budget * 0.4, 2)
        food = round(budget * 0.25, 2)
        travel = round(budget * 0.2, 2)

        # Trip type customization
        trip_context = {
            'solo': 'a solo traveler looking for independent activities, self-discovery, and flexibility',
            'family': 'a family with kids, focusing on family-friendly activities, safety, and entertainment for all ages',
            'couple': 'a couple looking for romantic experiences, restaurants, and activities suitable for two',
            'group': 'a group of friends looking for fun group activities, social experiences, and group-friendly venues'
        }

        context = trip_context.get(trip_type, trip_context['solo'])

        prompt = f"""
Create a detailed {days}-day travel itinerary for {destination} with a budget of ${budget}.

This is a {trip_type} trip for {context}.

Budget breakdown:
- Accommodation: ${stay}
- Food: ${food}
- Travel/Activities: ${travel}

Please provide:
- Day-by-day itinerary
- Activities suited for {trip_type}
- Restaurant suggestions
- Cost estimates
- Practical tips

Make it engaging and practical.
"""

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
        destination = ""
        trip_type = ""
        stay = food = travel = 0

    return render_template(
        "result.html",
        destination=destination,
        trip_type=trip_type,
        itinerary=itinerary_html,
        stay=stay,
        food=food,
        travel=travel
    )


# IMPORTANT for local testing only
if __name__ == "__main__":
    app.run()