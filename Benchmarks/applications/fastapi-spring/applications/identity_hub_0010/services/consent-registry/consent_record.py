# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/record_consent")
async def record_consent(request: Request):
    phrase = request.headers.get('host', '')
    pending = list(str(phrase).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    persona = ','.join(collected)
    requests.post("http://directory-sync:8080/SyncDirectory", json={"identity_payload": str(persona)})
    return {"updated": True}
