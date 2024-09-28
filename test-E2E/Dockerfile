FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    chromium-driver \
    chromium

WORKDIR /usr/src/app

COPY ./requirements.txt .
COPY ./test_selenium.py .

RUN pip install --no-cache-dir -r requirements.txt

ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_BIN=/usr/bin/chromedriver

CMD ["python", "test_selenium.py"]
