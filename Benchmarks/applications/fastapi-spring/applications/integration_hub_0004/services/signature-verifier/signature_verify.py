# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/verify_signature")
async def verify_signature(request: Request):
    summary = (await request.form()).get('field', '')
    handshake = (lambda v: v.strip())(summary)
    requests.post("http://retry-service:8080/QueueRetry", json={"integrations_payload": str(handshake)})
    return {"updated": True}
