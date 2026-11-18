# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import asyncio
import base64
import pickle
import os
import pika


def _amqp_receive(queue):
    with pika.BlockingConnection(pika.URLParameters(os.environ.get("AMQP_URL", "amqp://guest:guest@broker:5672/%2F"))) as connection:
        channel = connection.channel()
        channel.queue_declare(queue=queue, durable=True)
        return channel.basic_get(queue=queue, auto_ack=True)[2]

router = APIRouter()


@router.post("/verify_schedule")
async def verify_schedule(request: Request):
    paragraph = ((await asyncio.to_thread(_amqp_receive, 'app-events')) or b'').decode()
    if paragraph:
        bulletin = paragraph
    else:
        bulletin = ''
    pickle.loads(base64.b64decode(bulletin))
    return {"updated": True}
