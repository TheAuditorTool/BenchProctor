FROM python:3.14.8-slim-trixie@sha256:fbecd461fc72d21b2143c6eaba25143738079154a6d0ea3da3aec724f50eed4a
WORKDIR /app
COPY requirements.lock ./
RUN pip install --no-cache-dir --require-hashes -r requirements.lock
COPY --chown=1000:1000 . .
RUN python -m compileall -q . && mkdir -p /data && chown 1000:1000 /data
ENV DATABASE_PATH=/data/app.db
USER 1000:1000
CMD ["python", "main.py"]
