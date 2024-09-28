FROM python:3.9-slim

WORKDIR /app

COPY ./assets ./assets
COPY ./link_bio ./link_bio
COPY ./requirements.txt .
COPY ./rxconfig.py .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3000

CMD ["reflex", "run"]
