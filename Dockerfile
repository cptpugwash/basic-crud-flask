FROM python:2.7-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python create-database.py

EXPOSE 5000

CMD ["python", "run.py"]
