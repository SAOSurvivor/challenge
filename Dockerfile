FROM python:3.11-slim

# Install postgres client for waiting db container
RUN apt-get update && apt-get install --assume-yes postgresql-client

## Create default user:group for this container
RUN groupadd challenge;
RUN useradd -g challenge -ms /bin/bash challenge;

USER challenge

# add script to wait for db container to be ready
COPY ./docker/wait-for-postgres.sh /home/challenge/wait-for-postgres.sh

RUN pip3 install pipenv

WORKDIR /home/challenge/app
ENV PATH /home/challenge/.local/bin:${PATH}

COPY --chown=challenge:challenge Pipfile /home/challenge/Pipfile
COPY --chown=challenge:challenge Pipfile.lock /home/challenge/Pipfile.lock

RUN pipenv install --deploy --system --dev

ENV PYTHONPATH /home/challenge/app/

COPY --chown=challenge:challenge . /home/challenge/app
