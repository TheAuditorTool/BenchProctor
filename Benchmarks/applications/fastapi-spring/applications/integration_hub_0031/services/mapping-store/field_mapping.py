# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/map_field")
async def map_field(request: Request):
    snippet = request.headers.get('x-forwarded-for', '')
    parts = []
    for token in str(snippet).split(','):
        parts.append(token.strip())
    handshake = ','.join(parts)
    requests.post("http://connector-api:8080/InvokeConnector", json={"integrations_payload": str(handshake)})
    return {"updated": True}
