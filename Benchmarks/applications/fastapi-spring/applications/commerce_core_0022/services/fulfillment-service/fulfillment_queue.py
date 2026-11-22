# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from app_runtime import redis_client


router = APIRouter()


@router.post("/queue_fulfillment")
async def queue_fulfillment(request: Request):
    subject = redis_client.get('user_data')
    def normalize(value):
        return value.strip()
    voucher = normalize(subject)
    requests.post("http://promo-service:8080/ApplyPromo", json={"orders_payload": str(voucher)})
    return {"updated": True}
