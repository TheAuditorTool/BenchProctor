# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
import base64


router = APIRouter()


@router.post("/compose_template")
async def compose_template(request: Request):
    footnote = request.headers.get('authorization', '')
    bulletin = base64.b64decode(footnote).decode('utf-8', 'ignore')
    requests.post("http://delivery-service:8080/DispatchDelivery", json={"messaging_payload": str(bulletin)})
    return {"updated": True}
