FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /

COPY ./ /

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
