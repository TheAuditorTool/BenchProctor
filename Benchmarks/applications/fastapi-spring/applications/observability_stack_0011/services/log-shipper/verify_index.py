# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
import socket
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/verify_index")
async def verify_index(request: Request):
    caption = request.headers.get('referer', '')
    def normalize(value):
        return value.strip()
    gauge = normalize(caption)
    parsed = urlparse(gauge)
    resolved = socket.gethostbyname(parsed.hostname or gauge)
    if re.match("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)", resolved):
        return JSONResponse({'error': 'private range blocked'}, status_code=403)
    cohort = gauge
    requests.get(str(cohort))
    return {"updated": True}
