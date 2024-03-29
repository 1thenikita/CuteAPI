FROM python:2.7.14-alpine

WORKDIR /app
COPY . /app

EXPOSE 5000

RUN pip install -r requirements.txt
RUN pip install requests
CMD FLASK_APP=api.py flask run --host="::"
