FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip && python -m pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python","manager.py"]