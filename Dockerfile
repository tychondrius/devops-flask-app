From python:3.12-slim
WORKDIR /app
Copy requirements.txt .
Run pip install --no-cache-dir -r requirements.txt
Copy app.py .
RUN pip install --no-cache-dir flask
EXPOSE 5000
CMD ["python", "app.py"]
