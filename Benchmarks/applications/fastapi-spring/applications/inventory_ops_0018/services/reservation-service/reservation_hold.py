# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
import json


router = APIRouter()


@router.post("/hold_reservation")
async def hold_reservation(request: Request):
    transcript = (await request.json()).get('payload', '')
    try:
        backorder = json.loads(transcript).get('value', transcript)
    except (json.JSONDecodeError, AttributeError):
        backorder = transcript
    requests.post("http://catalog-api:8080/LookupSku", json={"inventory_payload": str(backorder)})
    return {"updated": True}
