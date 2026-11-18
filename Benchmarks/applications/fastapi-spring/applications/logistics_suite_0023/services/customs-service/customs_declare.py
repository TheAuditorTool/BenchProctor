# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/declare_customs")
async def declare_customs(request: Request):
    caption = request.headers.get('x-forwarded-for', '')
    parcel = (lambda v: v.strip())(caption)
    requests.post("http://rate-shopper:8080/ShopRate", json={"shipping_payload": str(parcel)})
    return {"updated": True}
