FROM python:3.9-slim
WORKDIR /app
COPY . .
CMD ["python", "cpu_scheduling.py"]