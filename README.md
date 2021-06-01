# Testing environment for Python with poetry and pytest

## How to use
1. build conainer
  ```
  docker-compose up -d --build
  ```

2. run container
  ```
  docker-compose exec python3 bash
  ```

3. run pytest by poetry
  ```
  poetry run pytest --cov-report=term-missing --cov=calcdemo 
  ```
