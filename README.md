# Echocart Assistant

**Echocart Assistant** is an AI-powered Chrome Extension integrated with a Flask backend that helps users analyze Amazon product pages intelligently.  
It leverages **Groq's LLaMA 3.1 model** to summarize reviews, analyze sentiments, extract pros & cons, and even compare products — all in real time.

---

## 🚀 Features

- 🧠 **AI Product Insights** — Get summaries, pros & cons, and detailed analyses of product reviews.
- ⚖️ **Product Comparison** — Compare two Amazon products side-by-side.
- 💬 **Interactive Chat** — Ask any question about a product and get an intelligent answer.
- 🌐 **Chrome Extension Integration** — Works directly on Amazon.com and Amazon.in pages.
- 🔐 **Groq API Integration** — Uses LLaMA 3.1 for fast and intelligent text understanding.

---


---

## ⚙️ Tech Stack

**Backend**
- Python 3.19
- Flask
- Flask-CORS
- Groq API (LLaMA 3.1 model)

**Frontend**
- Chrome Extension (Manifest V3)
- HTML, CSS, JavaScript

---

## 🧰 Installation & Setup

### 1️⃣ Clone this Repository

```bash
git clone https://github.com/pragyan2004/echocart-assistant.git
cd echocart-assistant
```

### 2️⃣ Setup the Backend

Navigate to the backend directory:

    cd ai


Install dependencies:

    pip install requirements.txt


Set up your Groq API key:

    export GROQ_API_KEY=your_groq_api_key


(On Windows use set GROQ_API_KEY=your_groq_api_key)

Run the Flask app:

    python app.py


The backend will start at: http://127.0.0.1:5000

### 3️⃣ Load the Chrome Extension

* Open Google Chrome → chrome://extensions/

* Enable Developer mode

* Click Load unpacked

* Select the extension folder from this project

* The Echocart Assistant icon will appear in your toolbar

### 🧪 Usage

* Go to any Amazon product page (e.g., amazon.com or amazon.in).

* Click on the Echocart Assistant icon in your browser toolbar.

* Use the following options:

    Summarize – Get a short summary of all customer reviews.

    Analyze – Understand strengths, weaknesses, and sentiment.

    Pros & Cons – View clear bullet points.

    Compare – Compare current product with another one.

    Chat – Ask any custom question about the product.

### 🧠 Example Request (Ask Endpoint)
```
POST /ask
Content-Type: application/json

{
  "title": "Echo Dot (5th Gen)",
  "description": "Smart speaker with Alexa.",
  "reviews": ["Great sound quality!", "Mic could be better."],
  "question": "Is this good for home automation?"
}
```

### 📸 Screenshots (Optional)

<img width="1913" height="979" alt="Screenshot 2025-11-12 103731" src="https://github.com/user-attachments/assets/1b72fd53-5ed1-4d4f-a931-f1167ea91ebd" />

<img width="495" height="743" alt="Screenshot 2025-11-12 103837" src="https://github.com/user-attachments/assets/534311ce-b629-4696-9c8f-3f4392f22521" />

<img width="492" height="747" alt="Screenshot 2025-11-12 103815" src="https://github.com/user-attachments/assets/d43b0a2b-70cb-44b9-9e2e-df7ca57d0566" />

<img width="476" height="749" alt="Screenshot 2025-11-12 103746" src="https://github.com/user-attachments/assets/fbed9c9d-2465-4149-8aa1-8ac164a5c614" />



