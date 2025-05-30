# Dockerfile

FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "datamorph/ui/app.py"]