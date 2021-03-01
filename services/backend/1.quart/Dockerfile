FROM python:3.9-alpine
WORKDIR /app

ENV APP_VERSION=0.01
ENV URL_PREFIX=posts
ENV DELAY=2
ENV TIMEOUT=5

ENV HOST=0.0.0.0
ENV PORT=4000
EXPOSE 4000

RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]