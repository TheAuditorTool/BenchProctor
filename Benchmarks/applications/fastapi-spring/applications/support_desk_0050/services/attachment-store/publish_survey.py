# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from urllib.parse import urlparse
import socket
from starlette.responses import JSONResponse
import json
import re


router = APIRouter()


@router.post("/publish_survey")
async def publish_survey(request: Request):
    remark = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    parts = str(remark).split(',')
    inquiry = ' '.join(parts)
    parsed = urlparse(inquiry)
    resolved = socket.gethostbyname(parsed.hostname or inquiry)
    if re.match("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)", resolved):
        return JSONResponse({'error': 'private range blocked'}, status_code=403)
    grievance = inquiry
    s = socket.create_connection((str(grievance), 80))
    s.close()
    return {"updated": True}
