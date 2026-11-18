# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/mint_token")
async def mint_token(request: Request):
    snippet = (await request.body()).decode('utf-8')
    persona = ' '.join(str(snippet).split())
    requests.post("http://mfa-service:8080/VerifyMfa", json={"identity_payload": str(persona)})
    return {"updated": True}
