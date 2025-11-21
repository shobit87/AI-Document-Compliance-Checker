# 🧠 AI Document Compliance Checker

An AI-powered document analysis and correction system built with **FastAPI**, **Streamlit**, and **OpenAI GPT models**.  
This tool evaluates business documents for **grammar**, **sentiment**, **clarity**, and **compliance**, and then automatically generates corrected and downloadable versions in **DOCX or PDF** format.

---

## 🚀 Features

- 🔍 **AI Document Analysis**
  - Grammar score (0–100)
  - Sentiment classification (positive / neutral / negative)
  - Clarity and compliance evaluation
  - Actionable recommendations

- ✍️ **AI Text Correction**
  - Automatically improves tone, punctuation, and readability
  - Generates corrected DOCX and PDF files

- 📑 **Auto Report Generation**
  - Produces structured compliance reports using GPT and Aspose

- 🧰 **Technology Stack**
  - **Backend:** FastAPI (Python 3.11)
  - **Frontend:** Streamlit
  - **AI Engine:** OpenAI GPT-4o-mini
  - **PDF Engine:** Aspose.Words (cross-platform, no MS Word required)
  - **Containerization:** Docker

---

## 🧱 Project Structure

AI-DOC-COMPLIANCE/
│
├── app/
│ ├── utils/
│ │ ├── init.py
│ │ ├── ai_agent.py # AI analysis logic using GPT
│ │ ├── docx_parser.py # Extracts text from DOCX files
│ │ ├── pdf_parser.py # Extracts text from PDF files
│ │ ├── helpers.py # Temp file handling & utilities
│ │ ├── sentiment_tools.py # Optional sentiment utilities
│ │ └── init.py
│ │
│ ├── main.py # FastAPI backend routes (/analyze_file, /correct_file)
│
├── generated_files/ # Stores corrected or exported output files
├── uploads/ # Stores uploaded files temporarily
│
├── venv/ # Virtual environment (ignored in git)
│
├── .gitignore # Git ignore rules
├── Dockerfile # Docker image configuration
├── README.md # Project documentation
├── requirements.txt # Python dependencies
└── .vscode/ # VS Code workspace settings

yaml
Copy code

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/shobit87/AI-Document-Compliance-Checker.git
cd AI-DOC-COMPLIANCE
2️⃣ Create a Virtual Environment
bash
Copy code
python -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Add Environment Variables
Create a .env file in the root directory:

bash
Copy code
OPENAI_API_KEY=sk-your-openai-api-key
🖥️ Running the Application
Start FastAPI Backend
bash
Copy code
uvicorn app.main:app --reload
Then open the API docs in your browser:
👉 http://127.0.0.1:8000/docs

Start Streamlit Frontend
bash
Copy code
streamlit run streamlit_app.py
Then visit the UI at:
👉 http://localhost:8501

🐳 Docker Deployment
You can also containerize and run both frontend & backend in Docker.

Build the image
bash
Copy code
docker build -t ai-doc-compliance .
Run the container
bash
Copy code
docker run -p 8000:8000 -p 8501:8501 --env-file .env ai-doc-compliance
Then visit:

API → http://localhost:8000/docs

UI → http://localhost:8501

🧹 Temporary File Handling
Uploaded and generated files are stored under /uploads and /generated_files.

Temporary files are automatically removed when the backend shuts down.

You can manually clear older generated files if needed.

📊 Example Output
Attribute	Example Output
Grammar Score	93 / 100
Sentiment	Neutral
Compliance Score	89%
Recommendations	- Simplify complex sentences
- Maintain consistent capitalization
- Improve section headings



👨‍💻 Author
Shobhit Kumar
Data Analyst | Business Analytics | AI & Automation


