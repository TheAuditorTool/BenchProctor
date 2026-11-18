# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/apply_promo")
async def apply_promo(request: Request):
    heading = request.headers.get('referer', '')
    def normalize(value):
        return value.strip()
    voucher = normalize(heading)
    requests.post("http://order-history:8080/LookupOrder", json={"orders_payload": str(voucher)})
    return {"updated": True}
