# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
import json


router = APIRouter()


@router.post("/start_recovery")
async def start_recovery(request: Request):
    paragraph = requests.get('https://api.partner.example.com/v1/profile').text
    persona = json.loads(paragraph).get('value', '')
    requests.post("http://session-store:8080/CreateSession", json={"identity_payload": str(persona)})
    return {"updated": True}
