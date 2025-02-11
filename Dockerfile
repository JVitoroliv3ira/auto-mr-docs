FROM python:3.12-slim

ENV POETRY_VERSION=2.0.1
WORKDIR /app

RUN pip install "poetry==$POETRY_VERSION"

COPY pyproject.toml poetry.lock ./

RUN poetry install --only main --no-root

COPY . .

ENTRYPOINT ["poetry", "run", "python", "auto_mr_docs/cli.py"]
