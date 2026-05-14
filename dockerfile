FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 7860

WORKDIR /app/code

CMD ["python", "app.py"]