FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

COPY . .

EXPOSE 8000

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
