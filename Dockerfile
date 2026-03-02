FROM python:3.9-slim
RUN pip install flask requests gunicorn
WORKDIR /app
COPY app.py .
EXPOSE 8080
CMD ["python", "app.py"]
