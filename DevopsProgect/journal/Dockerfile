FROM python:latest
WORKDIR /code

COPY /app/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY /app /code/

CMD flask db upgrade && flask run --host=0.0.0.0 --port=5000