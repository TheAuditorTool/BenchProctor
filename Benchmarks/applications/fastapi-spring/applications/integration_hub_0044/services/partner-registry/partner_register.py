# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/register_partner")
async def register_partner(request: Request):
    blurb = request.cookies.get('session_token', '')
    handshake = bytes.fromhex(blurb).decode('utf-8', 'ignore')
    requests.post("http://mapping-store:8080/MapField", json={"integrations_payload": str(handshake)})
    return {"updated": True}
