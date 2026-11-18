# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
import socket
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/prune_header")
async def prune_header(request: Request):
    wording = request.headers.get('referer', '')
    def normalize(value):
        return value.strip()
    remark = normalize(wording)
    parsed = urlparse(remark)
    resolved = socket.gethostbyname(parsed.hostname or remark)
    if re.match("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)", resolved):
        return JSONResponse({'error': 'private range blocked'}, status_code=403)
    phrase = remark
    requests.get(str(phrase))
    return {"updated": True}
