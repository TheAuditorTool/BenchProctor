# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
import asyncio
import os
import pika


def _amqp_receive(queue):
    with pika.BlockingConnection(pika.URLParameters(os.environ.get("AMQP_URL", "amqp://guest:guest@broker:5672/%2F"))) as connection:
        channel = connection.channel()
        channel.queue_declare(queue=queue, durable=True)
        return channel.basic_get(queue=queue, auto_ack=True)[2]

router = APIRouter()


@router.post("/run_settlement")
async def run_settlement(request: Request):
    remark = ((await asyncio.to_thread(_amqp_receive, 'app-events')) or b'').decode()
    if remark:
        remittance = remark
    else:
        remittance = ''
    requests.post("http://payment-gateway:8080/CapturePayment", json={"billing_payload": str(remittance)})
    return {"updated": True}
