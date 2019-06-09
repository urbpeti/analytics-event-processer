FROM python:3.6-alpine as application
ENV LC_ALL C.UTF-8
ENV LaND C.UTF-8

WORKDIR /app

RUN pip install pipenv

COPY Pipfile Pipfile.lock /app/

RUN pipenv install

EXPOSE 8000

COPY . /app/

CMD ["pipenv", "run", "gunicorn", "-b 0.0.0.0:8000", "-w 4", "app:app"]