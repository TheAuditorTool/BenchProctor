# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
import json


router = APIRouter()


@router.post("/register_partner")
async def register_partner(request: Request):
    wording = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    parts = []
    for token in str(wording).split(','):
        parts.append(token.strip())
    handshake = ','.join(parts)
    requests.post("http://mapping-store:8080/MapField", json={"integrations_payload": str(handshake)})
    return {"updated": True}
