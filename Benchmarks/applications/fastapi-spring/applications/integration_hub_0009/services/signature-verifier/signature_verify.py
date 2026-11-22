# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/verify_signature")
async def verify_signature(request: Request):
    heading = (await request.body()).decode('utf-8')
    handshake = heading.decode('utf-8', 'ignore') if isinstance(heading, bytes) else heading
    requests.post("http://connector-api:8080/InvokeConnector", json={"integrations_payload": str(handshake)})
    return {"updated": True}
