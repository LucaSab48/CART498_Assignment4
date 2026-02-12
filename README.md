# Lynch's Dream Machine

A Flask web app that interprets user-submitted dreams in a Jungian voice and generates a symbolic image inspired by David Lynch's atmosphere.

## Entry Point

The application entry point is `app.py`.

- Local development command: `python app.py`
- Main route handler: `index()` at `/`
- Startup block:

```python
if __name__ == "__main__":
    app.run(debug=True)
```

## Tech Stack

- Python + Flask
- OpenAI API (`gpt-4.1` for text, `gpt-image-1` for image generation)
- Jinja templates in `templates/` and static assets in `static/`

## Setup

1. Create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install flask python-dotenv openai gunicorn
```

3. Add your API key to `.env`:

```env
OPENAI_API_KEY=your_api_key_here
```

## Run Locally

```powershell
python app.py
```

Then open `http://127.0.0.1:5000`.

## App Flow

1. User submits a dream in the form.
2. The app generates a Jungian-style interpretation (`gpt-4.1`).
3. The interpretation is reduced to symbolic cues (mood, setting, elements).
4. Those cues are used to build a safer image prompt.
5. The app generates and displays an image (`gpt-image-1`).

## Testing

There are currently no automated tests in this repository.

To run tests once available:

```powershell
pip install pytest
python -m pytest
```

Current expected behavior in this repo: `pytest` reports no tests collected (after installation).
