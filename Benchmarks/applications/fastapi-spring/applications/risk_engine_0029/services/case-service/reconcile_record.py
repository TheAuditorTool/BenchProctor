# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
import socket
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/reconcile_record")
async def reconcile_record(request: Request):
    subject = request.headers.get('x-forwarded-for', '')
    grievance = (lambda v: v.strip())(subject)
    parsed = urlparse(grievance)
    resolved = socket.gethostbyname(parsed.hostname or grievance)
    if re.match("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)", resolved):
        return JSONResponse({'error': 'private range blocked'}, status_code=403)
    verdict = grievance
    requests.get(str(verdict))
    return {"updated": True}
