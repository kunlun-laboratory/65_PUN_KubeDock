FROM python:3.12 AS base
# FROM python:3.10-rc AS base for mac

# RUN adduser --disabled-password --gecos '' appuser
# USER appuser
WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install --user -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["python", "app.py"]