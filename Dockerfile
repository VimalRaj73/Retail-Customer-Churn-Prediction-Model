FROM python:3.13-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "churn_prediction_app.py", "--server.address=0.0.0.0", "--server.port=8501"]