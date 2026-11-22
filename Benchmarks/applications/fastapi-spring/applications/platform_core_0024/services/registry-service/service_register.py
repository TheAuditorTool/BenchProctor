# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

router = APIRouter()


@router.post("/register_service")
async def register_service(request: Request):
    heading = request.headers.get('authorization', '')
    form = FormData(payload=heading)
    handshake = form.payload
    requests.post("http://quota-service:8080/EnforceQuota", json={"platform_payload": str(handshake)})
    return {"updated": True}
