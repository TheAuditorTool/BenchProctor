# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/place_order")
async def place_order(request: Request):
    memo = request.cookies.get('session_token', '')
    def normalize(value):
        return value.strip()
    voucher = normalize(memo)
    requests.post("http://cart-service:8080/UpdateCart", json={"orders_payload": str(voucher)})
    return {"updated": True}
