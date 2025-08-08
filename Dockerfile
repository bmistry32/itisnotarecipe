FROM python:3.12.2-slim-buster

EXPOSE 8000 

RUN pip install poetry==1.6.1

WORKDIR /itisnotarecipe

COPY ./pyproject.toml ./poetry.lock  /itisnotarecipe/
RUN poetry install

COPY . /itisnotarecipe/
VOLUME /recipes

ENTRYPOINT [ "bash", "create" ]
