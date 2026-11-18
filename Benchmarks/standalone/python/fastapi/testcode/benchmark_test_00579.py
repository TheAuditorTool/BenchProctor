# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import asyncio
import socket
import os
import pika
from fastapi.responses import JSONResponse


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


@app.post("/BenchmarkTest00579")
async def BenchmarkTest00579(request: Request):
    msg_value = ((await asyncio.to_thread(_amqp_receive, 'app-events')) or b'').decode()
    data = str(msg_value).replace('\x00', '')
    s = socket.create_connection((str(data), 80))
    s.close()
    return {"updated": True}
