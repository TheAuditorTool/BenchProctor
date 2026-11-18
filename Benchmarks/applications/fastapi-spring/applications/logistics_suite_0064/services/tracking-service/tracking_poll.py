# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from app_runtime import db


router = APIRouter()


@router.post("/poll_tracking")
async def poll_tracking(request: Request):
    transcript = db.fetch_one('SELECT text FROM comments LIMIT 1')
    parts = str(transcript).split(',')
    parcel = ' '.join(parts)
    requests.post("http://shipping-api:8080/QuoteShipment", json={"shipping_payload": str(parcel)})
    return {"updated": True}
