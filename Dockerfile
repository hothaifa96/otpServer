FROM python:3.10.8-slim-buster
EXPOSE 5002
ENV FLASK_APP main.py
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt
COPY . .
CMD flask run