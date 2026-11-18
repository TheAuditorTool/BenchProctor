# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from starlette.responses import JSONResponse
import asyncio
import re
from app_runtime import db
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


@app.post("/BenchmarkTest00011")
async def BenchmarkTest00011(request: Request):
    msg_value = ((await asyncio.to_thread(_amqp_receive, 'app-events')) or b'').decode()
    if not re.fullmatch("^(asc|desc|name|created)$", str(msg_value)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = msg_value
    db.execute('SELECT * FROM users ORDER BY ' + str(processed))
    return {"updated": True}
