from flask import Flask, render_template, request
import os
import google.generativeai as genai

app = Flask(__name__)

# Configure API key safely
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("❌ ERROR: GEMINI_API_KEY is not set!")

genai.configure(api_key=API_KEY)


# Bio generation function
def generate_bio(career, personality, interests, relationship_goals):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash-latest")

        prompt = f"""
        Generate a short dating bio:
        Career: {career}
        Personality: {personality}
        Interests: {interests}
        Relationship Goals: {relationship_goals}
        """

        response = model.generate_content(prompt)

        print("FULL RESPONSE:", response)

        if response and hasattr(response, "text") and response.text:
            return response.text.strip()
        else:
            return " No response from AI."

    except Exception as e:
        print(" REAL ERROR:", str(e)) 
        return f"ERROR: {str(e)}"


@app.route("/", methods=["GET", "POST"])
def home():
    bio = None

    if request.method == "POST":
        try:
            career = request.form.get("career", "")
            personality = request.form.get("personality", "")
            interests = request.form.get("interests", "")
            relationship_goals = request.form.get("relationship_goals", "")

            # Validate inputs
            if not all([career, personality, interests, relationship_goals]):
                bio = "⚠️ Please fill all fields."
            else:
                bio = generate_bio(career, personality, interests, relationship_goals)

        except Exception as e:
            print("🔥 FORM ERROR:", str(e))
            bio = "❌ Error processing your request."

    return render_template("index.html", bio=bio)


if __name__ == "__main__":
    app.run(debug=True)
