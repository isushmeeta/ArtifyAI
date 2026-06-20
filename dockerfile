FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

RUN python download_models.py

EXPOSE 7860

CMD ["python", "code/app.py"]