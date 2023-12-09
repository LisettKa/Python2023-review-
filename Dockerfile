FROM python:3.10
LABEL authors="liza"

VOLUME /app/data
EXPOSE 5000

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python", "app.py"]