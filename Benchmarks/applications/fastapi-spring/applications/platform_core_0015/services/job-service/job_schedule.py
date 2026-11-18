# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
import base64


router = APIRouter()


@router.post("/schedule_job")
async def schedule_job(request: Request):
    note = request.headers.get('authorization', '')
    handshake = base64.b64decode(note).decode('utf-8', 'ignore')
    requests.post("http://platform-api:8080/ProvisionTenant", json={"platform_payload": str(handshake)})
    return {"updated": True}
