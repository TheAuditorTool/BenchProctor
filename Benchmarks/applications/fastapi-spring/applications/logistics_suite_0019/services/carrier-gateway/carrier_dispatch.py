# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/dispatch_carrier")
async def dispatch_carrier(request: Request):
    citation = (await request.form()).get('field', '')
    pending = list(str(citation).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    parcel = ','.join(collected)
    requests.post("http://shipping-api:8080/QuoteShipment", json={"shipping_payload": str(parcel)})
    return {"updated": True}
