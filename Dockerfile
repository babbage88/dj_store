# syntax=docker/dockerfile:1
FROM python:3.11-slim-bookworm

# The installer requires curl (and certificates) to download the release archive
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates

# Download the latest installer
ADD https://astral.sh/uv/install.sh /uv-installer.sh

# Run the installer then remove it
RUN sh /uv-installer.sh && rm /uv-installer.sh

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.cargo/bin/:$PATH"

COPY --from=ghcr.io/astral-sh/uv:0.6.6 /uv /bin/uv

# Copy the project into the image
WORKDIR /app
COPY . /app

# Copy the local package or dependencies (adjust path accordingly)
# COPY /path/to/local/package /app/path/to/local/package

RUN uv venv

ENV PATH="/app/.venv/bin:$PATH"

RUN uv sync

# Port to expose (change if needed)
EXPOSE 8000

# Default CMD to run Gunicorn with 4 workers and auto-bind
CMD ["gunicorn", "store_mg.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "4", "--threads", "2"]
