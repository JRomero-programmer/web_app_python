FROM python:3.9-slim

WORKDIR /app

COPY ./link_bio/assets ./assets
COPY ./link_bio/link_bio ./link_bio
COPY ./link_bio/requirements.txt .
COPY ./link_bio/rxconfig.py .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3000

CMD ["reflex", "run"]
