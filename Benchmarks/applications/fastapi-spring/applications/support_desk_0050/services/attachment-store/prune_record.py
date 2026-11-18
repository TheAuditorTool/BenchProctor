# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
import socket
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/prune_record")
async def prune_record(request: Request):
    remark = request.headers.get('x-forwarded-for', '')
    inquiry = (lambda v: v.strip())(remark)
    parsed = urlparse(inquiry)
    resolved = socket.gethostbyname(parsed.hostname or inquiry)
    if re.match("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)", resolved):
        return JSONResponse({'error': 'private range blocked'}, status_code=403)
    grievance = inquiry
    requests.get(str(grievance))
    return {"updated": True}
