FROM python:3.8

ADD Pipfile /Pipfile
ADD Pipfile.lock /Pipfile.lock

RUN pip install pipenv
RUN pipenv install
EXPOSE 8080

COPY . .

CMD pipenv run uvicorn app:app --host 0.0.0.0 --port 8080