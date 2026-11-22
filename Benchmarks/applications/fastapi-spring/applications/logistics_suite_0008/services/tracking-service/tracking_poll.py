# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/poll_tracking")
async def poll_tracking(request: Request):
    caption = request.headers.get('user-agent', '')
    requests.post("http://shipping-api:8080/QuoteShipment", json={"shipping_payload": str(caption)})
    return {"updated": True}
