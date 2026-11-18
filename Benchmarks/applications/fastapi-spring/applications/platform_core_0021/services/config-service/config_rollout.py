# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
import base64


router = APIRouter()


@router.post("/rollout_config")
async def rollout_config(request: Request):
    excerpt = request.cookies.get('session_token', '')
    handshake = base64.b64decode(excerpt).decode('utf-8', 'ignore')
    requests.post("http://platform-api:8080/ProvisionTenant", json={"platform_payload": str(handshake)})
    return {"updated": True}
