FROM python:3.10.2-alpine
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 3000
CMD ["gunicorn", "src.api:app", "--bind", "0.0.0.0:3000"]