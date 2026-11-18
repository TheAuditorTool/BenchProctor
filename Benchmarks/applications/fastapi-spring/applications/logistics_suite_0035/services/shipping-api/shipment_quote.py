# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/quote_shipment")
async def quote_shipment(request: Request):
    phrase = request.headers.get('x-forwarded-for', '')
    parts = []
    for token in str(phrase).split(','):
        parts.append(token.strip())
    parcel = ','.join(parts)
    requests.post("http://customs-service:8080/DeclareCustoms", json={"shipping_payload": str(parcel)})
    return {"updated": True}
