FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

# SECRET_KEY must be provided at runtime (e.g. `docker run -e SECRET_KEY=...`)
# so the database is created at container start, not at build time.
CMD ["sh", "-c", "python create-database.py && python run.py"]
