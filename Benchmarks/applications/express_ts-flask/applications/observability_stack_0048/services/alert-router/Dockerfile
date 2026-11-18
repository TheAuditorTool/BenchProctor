FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY --chown=1000:1000 . .
RUN python -m compileall -q . && mkdir -p /data && chown 1000:1000 /data
ENV DATABASE_PATH=/data/app.db
USER 1000:1000
CMD ["python", "main.py"]
