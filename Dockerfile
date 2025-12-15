# Use a lightweight Python image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /usr/src/app

# Copy requirements and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Download required spaCy model
RUN python -m spacy download en_core_web_sm

# Default command to run the API

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
