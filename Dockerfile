FROM python:3.11-slim

WORKDIR /app

# Installa uv
RUN pip install --no-cache-dir uv

# Copia le dipendenze e installa
COPY pyproject.toml .
RUN uv pip install --system pyproject.toml

# Copia il codice sorgente
COPY src/ ./src
COPY entrypoints/ ./entrypoints

ENV PYTHONPATH=/app/src

CMD ["python", "entrypoints/run.py"]
