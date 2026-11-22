# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import asyncio
import re
import os
import pika


def _amqp_receive(queue):
    with pika.BlockingConnection(pika.URLParameters(os.environ.get("AMQP_URL", "amqp://guest:guest@broker:5672/%2F"))) as connection:
        channel = connection.channel()
        channel.queue_declare(queue=queue, durable=True)
        return channel.basic_get(queue=queue, auto_ack=True)[2]

app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00292")
async def BenchmarkTest00292(request: Request):
    msg_value = ((await asyncio.to_thread(_amqp_receive, 'app-events')) or b'').decode()
    parts = []
    for token in str(msg_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    parsed = urlparse(data)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", data) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    target_url = data
    requests.get(str(target_url))
    return {"updated": True}
