# 🧠 Mistral Intelligent OCR

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit)
![Mistral AI](https://img.shields.io/badge/Mistral%20AI-Powered-orange?style=for-the-badge)

A smart Optical Character Recognition (OCR) application powered by **Mistral AI**. This tool extracts text from images (handwritten or digital) and converts it into editable Markdown format with high accuracy.

---

## 📂 Project Structure

Here is how the project files are organized:

```text
MISTRAL-OCR-PROJECT/
│
├── .gitignore             # Files to ignore (venv, secrets, etc.)
├── README.md              # Project documentation
├── requirements.txt       # List of python dependencies
├── test_ocr.py            # Main Application Code (Streamlit)
│
└── venv/                  # Virtual Environment (Not uploaded to GitHub)


---
🚀 Features
📄 High Accuracy Extraction: Uses the mistral-ocr-latest model to understand complex document layouts.

📱 Mobile Ready: Fully responsive UI that works on desktops, tablets, and mobile phones.

📷 Camera Support: Take photos directly from your mobile browser to extract text.

🔒 Secure: API keys are handled via Streamlit Secrets (for Cloud) or secure input (for Local).

📥 Export Options: Copy text to clipboard or download as a .txt file.

---
🛠️ Tech Stack
Frontend: Streamlit

AI Model: Mistral AI

Language: Python


---
⚙️ Installation & Local Setup
Follow these steps to run the project on your own computer.

1. Clone the Repository
Bash

git clone [https://github.com/YOUR_USERNAME/mistral-ocr-app.git](https://github.com/YOUR_USERNAME/mistral-ocr-app.git)
cd mistral-ocr-app
2. Create Virtual Environment
Bash

# Windows
python -m venv venv
.\venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
3. Install Requirements
Bash

pip install -r requirements.txt
4. Run the App
Bash

streamlit run test_ocr.py

---
🔑 How to Configure API Key
You need a Mistral API Key to use this app. Get it here: Mistral Console.

Method 1: Quick Use (UI)

Run the app.

Paste your key in the Sidebar input field.

Method 2: Persistent (Secrets File)

Create a folder named .streamlit in your project root.

Create a file inside it named secrets.toml.

Add your key:

Ini, TOML

MISTRAL_API_KEY = "your_actual_api_key_here"
🌐 Deploying to the Web
To make this app public for everyone:

Push code to GitHub.

Login to Streamlit Cloud.

Click "New App" and select this repository.

Go to Advanced Settings -> Secrets and paste:

Ini, TOML

MISTRAL_API_KEY = "your_api_key_here"
Click Deploy.

---
👤 Author
Gopal Rajbhar

Python Developer | AI Enthusiast