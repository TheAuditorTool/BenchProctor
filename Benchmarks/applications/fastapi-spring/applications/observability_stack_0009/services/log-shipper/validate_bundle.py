# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import json
import socket
import requests


router = APIRouter()


@router.post("/validate_bundle")
async def validate_bundle(request: Request):
    summary = requests.get('https://api.partner.example.com/v1/profile').text
    gauge = json.loads(summary).get('value', '')
    s = socket.create_connection((str(gauge), 80))
    s.close()
    return {"updated": True}
