import os
import base64
from dotenv import load_dotenv
from groq import Groq
import PyPDF2
import docx

load_dotenv()
client = Groq(api_key=os.getenv("gsk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"))

SYSTEM_PROMPT = """You are Intellexa, a focused AI study assistant. You ONLY answer questions related to:

* Education (subjects, concepts, homework, exams, study techniques, academic writing)
* Career guidance (career paths, career advice, resume tips, interviews, skills development)
* Job opportunities (job searching, internships, job roles, qualifications needed)
* Industry trends (market trends, industry insights, business sectors, emerging technologies in a professional context)
* Current Affairs (national and international events, government initiatives, economic developments, important news, science and technology updates)
* General Knowledge (history, geography, science, environment, important personalities, organizations, awards, books, and commonly asked competitive exam topics)

If the user asks about ANYTHING outside these topics — such as entertainment gossip, celebrity news, sports predictions, personal relationships, cooking, gaming, jokes, fictional roleplay, or other unrelated subjects — you must politely decline with this message:

"I'm sorry, I can only assist with education, career guidance, job opportunities, industry & market trends, current affairs, and general knowledge. Please ask me something related to these topics and I'll be happy to help! 📚"

Do NOT answer off-topic questions even if the user insists or reframes them. Stay focused and helpful within your scope.

Keep answers:

* Clear and concise
* Accurate and educational
* Well-structured with examples when useful
* Suitable for students, job seekers, and lifelong learners

When relevant, provide step-by-step explanations, practical examples, and actionable guidance."""


def get_ai_response(user_input, chat_history=None):
    if chat_history is None:
        chat_history = []

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    for entry in chat_history:
        messages.append(entry)
    messages.append({"role": "user", "content": user_input})

    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.7,
            max_tokens=1024,
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"


def extract_text_from_file(uploaded_file):
    """Extracts text from PDF, DOCX, or TXT files."""
    try:
        if uploaded_file.type == "application/pdf":
            reader = PyPDF2.PdfReader(uploaded_file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""
            return text.strip()

        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            doc = docx.Document(uploaded_file)
            return "\n".join([para.text for para in doc.paragraphs]).strip()

        elif uploaded_file.type == "text/plain":
            return uploaded_file.read().decode("utf-8").strip()

        else:
            return None
    except Exception as e:
        return f"Error reading file: {str(e)}"


def get_ai_response_with_image(user_input, image_bytes):
    """Sends an image + question to a Groq vision model."""
    try:
        base64_image = base64.b64encode(image_bytes).decode("utf-8")

        completion = client.chat.completions.create(
            model="llama-3.2-90b-vision-preview",
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": user_input or "Explain what is shown in this image in an educational context."},
                        {
                            "type": "image_url",
                            "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}
                        }
                    ]
                }
            ],
            temperature=0.7,
            max_tokens=1024,
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    print("Testing chatbot.py...")
    print(get_ai_response("Hello!"))
