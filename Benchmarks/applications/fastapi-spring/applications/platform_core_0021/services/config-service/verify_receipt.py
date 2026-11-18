# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
import socket
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/verify_receipt")
async def verify_receipt(request: Request):
    excerpt = request.headers.get('referer', '')
    def normalize(value):
        return value.strip()
    handshake = normalize(excerpt)
    parsed = urlparse(handshake)
    resolved = socket.gethostbyname(parsed.hostname or handshake)
    if re.match("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)", resolved):
        return JSONResponse({'error': 'private range blocked'}, status_code=403)
    persona = handshake
    requests.get(str(persona))
    return {"updated": True}
