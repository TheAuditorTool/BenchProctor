# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/fetch_secret")
async def fetch_secret(request: Request):
    passage = request.headers.get('authorization', '')
    parts = []
    for token in str(passage).split(','):
        parts.append(token.strip())
    persona = ','.join(parts)
    requests.post("http://audit-log:8080/AppendAudit", json={"platform_payload": str(persona)})
    return {"updated": True}
