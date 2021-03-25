FROM python:3.9-alpine

COPY requirements.txt .
WORKDIR .
RUN pip install -r requirements.txt
EXPOSE 9092
COPY . .

CMD ["python", "consumer.py"]