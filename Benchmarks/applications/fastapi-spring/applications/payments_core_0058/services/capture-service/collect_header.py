# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import json
import socket
import requests


router = APIRouter()


@router.post("/collect_header")
async def collect_header(request: Request):
    caption = requests.get('https://api.partner.example.com/v1/profile').text
    ledger = json.loads(caption).get('value', '')
    s = socket.create_connection((str(ledger), 80))
    s.close()
    return {"updated": True}
