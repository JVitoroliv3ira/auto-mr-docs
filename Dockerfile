FROM python:3.12-alpine AS builder

WORKDIR /app

RUN apk add --no-cache gcc musl-dev libffi-dev libc6-compat

COPY pyproject.toml README.md ./
RUN poetry lock --no-interaction

RUN pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false \
    && poetry install --without dev --no-interaction --no-root

COPY . .

RUN poetry build

RUN apk del gcc musl-dev libffi-dev

FROM python:3.12-alpine

WORKDIR /app

COPY --from=builder /app/dist/*.whl ./

RUN pip install --no-cache-dir --no-compile ./*.whl \
    && rm -rf /root/.cache/pip

ENTRYPOINT ["/bin/sh", "-c"]
CMD ["auto-mr-docs --help"]
