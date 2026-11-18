# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import json
import socket
import requests


router = APIRouter()


@router.post("/format_bundle")
async def format_bundle(request: Request):
    citation = requests.get('https://api.partner.example.com/v1/profile').text
    backorder = json.loads(citation).get('value', '')
    s = socket.create_connection((str(backorder), 80))
    s.close()
    return {"updated": True}
