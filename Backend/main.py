from flask import Flask, render_template, request
import os
import google.generativeai as genai
import warnings
from dotenv import load_dotenv  # If using .env for API key

# Load environment variables from .env
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Suppress deprecation warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Configure Gemini API with the API key from environment
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Define the bio generation function using the Gemini API
def generate_bio(career, personality, interests, relationship_goals):
    model = genai.GenerativeModel("gemini-1.5-flash")  # Or "gemini-pro"
    prompt = f"Generate a bio for a {personality} {career} who enjoys {interests} and is looking for {relationship_goals}."
    response = model.generate_content(prompt)
    
    if response:
        return response.text.strip()
    return "Error generating bio."

# Flask route for the home page
@app.route("/", methods=["GET", "POST"])
def home():
    bio = None  # Initialize bio as None by default
    if request.method == "POST":
        career = request.form["career"]
        personality = request.form["personality"]
        interests = request.form["interests"]
        relationship_goals = request.form["relationship_goals"]

        # Call the function to generate the bio
        bio = generate_bio(career, personality, interests, relationship_goals)
    
    return render_template("index.html", bio=str(bio))

if __name__ == "__main__":
    app.run(debug=True)
