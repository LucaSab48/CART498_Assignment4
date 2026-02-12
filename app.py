from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

JUNG_SYSTEM_PROMPT = """
You are an AI trained in Carl Jung’s analytical psychology,
influenced by the atmospheric and symbolic sensibility of David Lynch.

Interpret dreams symbolically, not literally.
Focus on archetypes, emotional tension, and unconscious patterns.

Write concisely.
Use poetic but restrained language.
Allow ambiguity.
Avoid academic tone and definitive conclusions.
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
                max_output_tokens=180
            )

            interpretation = text_response.output_text

            # --- SYMBOLIC ABSTRACTION (KEY FIX) ---
            # We do NOT pass free text into the image model.
            # We distill it into controlled symbolic elements.

            symbolic_prompt = client.responses.create(
                model="gpt-4.1",
                input=[
                    {
                        "role": "system",
                        "content": (
                            "Extract symbolic image cues from the following dream interpretation. "
                            "Return ONLY short, neutral phrases under these headings:\n"
                            "- Mood\n"
                            "- Setting\n"
                            "- Symbolic elements\n\n"
                            "Avoid violent, explicit, or distressing language."
                        )
                    },
                    {"role": "user", "content": interpretation}
                ],
                temperature=0.5,
                max_output_tokens=80
            )

            symbolic_cues = symbolic_prompt.output_text

            # --- IMAGE GENERATION (SAFE & PERSONALIZED) ---
            image_prompt = f"""
A surreal, cinematic dream image inspired by Jungian psychology
and the visual language of David Lynch.

Symbolic cues:
{symbolic_cues}

Visual style:
theatrical composition, symbolic interiors,
red curtains, deep shadows, controlled lighting,
minimal figures, mid-century surrealism,
dreamlike stillness.

The image should feel staged, symbolic, and unresolved.
Do not depict literal events.
Do not depict violence, danger, or explicit fear.
Focus on atmosphere and symbolism.
"""

            img = client.images.generate(
                model="gpt-image-1",
                prompt=image_prompt,
                size="auto",
                quality = "low"
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
