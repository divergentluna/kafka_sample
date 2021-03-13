FROM python:3.9-alpine

COPY . .
WORKDIR .
RUN pip install -r requirements.txt
EXPOSE 9092

CMD ['python', 'consumer.py']