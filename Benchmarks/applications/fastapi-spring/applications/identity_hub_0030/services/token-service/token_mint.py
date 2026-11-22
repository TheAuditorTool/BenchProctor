# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from security import require_login


router = APIRouter()


@router.post("/mint_token/{id}")
@require_login
async def mint_token(request: Request, id: str):
    tagline = request.path_params.get('id', '')
    collected = None
    def on_ready(value):
        nonlocal collected
        collected = value
    on_ready(tagline)
    persona = collected
    requests.post("http://session-store:8080/CreateSession", json={"identity_payload": str(persona)})
    return {"updated": True}
