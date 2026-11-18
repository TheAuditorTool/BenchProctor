# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
import socket
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/prune_config")
async def prune_config(request: Request):
    footnote = request.headers.get('x-forwarded-for', '')
    consignment = (lambda v: v.strip())(footnote)
    parsed = urlparse(consignment)
    resolved = socket.gethostbyname(parsed.hostname or consignment)
    if re.match("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)", resolved):
        return JSONResponse({'error': 'private range blocked'}, status_code=403)
    parcel = consignment
    requests.get(str(parcel))
    return {"updated": True}
