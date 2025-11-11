# ===============================
# AI Document Compliance - Dockerfile
# ===============================

# 1️⃣ Base Image
FROM python:3.11-slim

# 2️⃣ Set working directory inside the container
WORKDIR /app

# 3️⃣ Copy all project files into container
COPY . /app

# 4️⃣ Install system dependencies for PyMuPDF and Java (required by LanguageTool)
RUN apt-get update && apt-get install -y \
    build-essential \
    poppler-utils \
    openjdk-17-jre-headless \
    && apt-get clean

# 5️⃣ Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 6️⃣ Expose the FastAPI default port
EXPOSE 8000

# 7️⃣ Run the FastAPI app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
