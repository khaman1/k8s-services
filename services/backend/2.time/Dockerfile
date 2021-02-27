FROM python:3.9-alpine
WORKDIR /app

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

ENV APP_VERSION=0.01
ENV URL_PREFIX=time
ENV FLASK_RUN_PORT=4001
EXPOSE 4001

RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["flask", "run"]