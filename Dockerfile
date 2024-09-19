# Start with the FastAPI base image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir firebase-admin pydantic
EXPOSE 8001
