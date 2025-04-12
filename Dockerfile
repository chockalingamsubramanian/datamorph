# Dockerfile

FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir .

EXPOSE 8501

CMD ["calculator"]
