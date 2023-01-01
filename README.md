# auth0-demo
A test project of Auth0 integration on django w/ django-ninja

## Setup

### Local direnv setup
Install dependencies
```sh
brew install direnv
brew install pipenv
brew install postgresql
brew install python@3.10
```

Add `<PROJECT_ROOT_DIR>/app/.envrc`

```
layout python <PYTHON_DIR>
dotenv <PROJECT_ROOT_DIR>/.env.local
```

```sh
cd <PROJECT_ROOT_DIR>/app
direnv allow .
source .direnv/python-<PYTHON_VERSION>/bin/activate
pipenv install --dev
```


### Local Docker setup
install [Docker Desktop](https://www.docker.com/products/docker-desktop/)

build and run containers
```sh
cd <PROJECT_ROOT_DIR>
docker-compose build
docker-compose up -d
```
