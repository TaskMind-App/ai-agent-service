# נשתמש בגרסה קלה של פייתון
FROM python:3.10-slim

# הגדרת תיקיית העבודה
WORKDIR /app

# העתקת קובץ הדרישות והתקנתן
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# העתקת כל הקוד של הסרוויס
COPY . .

# הפורט של FastAPI
EXPOSE 8000

# הרצת השרת
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]