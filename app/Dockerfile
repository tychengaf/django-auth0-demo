# pull official base image
FROM python:3.10.8-slim

# setup env
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

# set work directory
WORKDIR /usr/src/app

# copy project
COPY . .

# install pipenv and compilation dependencies
RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends libpq-dev gcc

# install python dependencies
RUN pipenv install --system --dev --deploy && pipenv --clear

# run entrypoint.sh
RUN sed -i 's/\r$//g' entrypoint.sh
RUN chmod +x entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
