FROM python:3.11.17-slim-trixie@sha256:b7a9e5f6a93d6d4a31f129bbd4bdee69efccb6ded0fb230d78aafaf37af98377
WORKDIR /app
COPY requirements.lock ./
RUN pip install --no-cache-dir --require-hashes -r requirements.lock
COPY --chown=1000:1000 . .
RUN python -m compileall -q . && mkdir -p /data && chown 1000:1000 /data
ENV DATABASE_PATH=/data/app.db
USER 1000:1000
CMD ["python", "main.py"]
