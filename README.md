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

3. poetry update
  ```
  poetry update
  ```

4. run pytest by poetry
  ```
  poetry run pytest --cov-report=html --cov=calcdemo 
  ```
