from flask import Flask, render_template, request
import os
import base64
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

JUNG_SYSTEM_PROMPT = """
You are an AI trained in Carl Jung’s analytical psychology, also influenced by David Lynch's work.

Interpret dreams symbolically, not literally. 
Focus on archetypes, the collective unconscious,
emotional tone, and individuation.

Write concisely. 
Use poetic, unsettling language.
Allow for ambiguity.
Avoid academic tone. 
Avoid conclusions, but convey interpretations. 
"""

@app.route("/", methods=["GET", "POST"])
def index():
    interpretation = None
    image_data = None

    if request.method == "POST":
        dream = request.form["dream"]

        try:
            # --- TEXT INTERPRETATION ---
            text_response = client.responses.create(
                model="gpt-4.1",
                input=[
                    {"role": "system", "content": JUNG_SYSTEM_PROMPT},
                    {"role": "user", "content": dream}
                ],
                temperature=1.0,
                max_output_tokens=200
            )

            interpretation = text_response.output_text

            # --- IMAGE GENERATION ---
            image_prompt = f"""
            Create a surreal image inspired by David Lynch and Jungian psychology.

            Dream:
            {dream}

            Interpretation:
            {interpretation}

            Mood:
            uncanny, quiet, ominous, theatrical, surreal
            
            Visual language:
            red curtains, harsh lighting, deep shadows,
            empty interiors, symbolic figures,
            mid-century surrealism, dream logic
            
            Do not illustrate literally.
            Create an image that feels staged, symbolic, and unresolved.
            """

            img = client.images.generate(
                model="gpt-image-1",
                prompt=image_prompt,
                size="auto"
            )
            
            image_data = img.data[0].b64_json



        except Exception as e:
            interpretation = f"Error: {str(e)}"

    return render_template(
        "index.html",
        interpretation=interpretation,
        image_data=image_data
    )

if __name__ == "__main__":
    app.run(debug=True)


