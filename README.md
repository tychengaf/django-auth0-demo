# django-auth0-demo
A test project of Auth0 integration on django w/ django-ninja

## Setup

### Local direnv setup (Mac)

1. Install [Homebrew](https://brew.sh/)

2. Install dependencies
  ```sh
  brew install direnv
  brew install pipenv
  brew install postgresql
  brew install python@3.10
  ```
3. Follow the [direnv install guide](https://direnv.net/docs/installation.html) to [hook direnv to your shell](https://direnv.net/docs/hook.html)

4. Add `<PROJECT_ROOT_DIR>/app/.envrc`

  ```
  layout python <PYTHON_DIR>
  dotenv <PROJECT_ROOT_DIR>/.env.local
  ```

5. Activate virtual env and install python dependencies
  ```sh
  cd <PROJECT_ROOT_DIR>/app
  direnv allow .
  source .direnv/python-<PYTHON_VERSION>/bin/activate
  pipenv install --dev
  ```


### Local Docker setup

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)

2. Build and run containers
  ```sh
  cd <PROJECT_ROOT_DIR>
  docker-compose build
  docker-compose up -d
  ```
