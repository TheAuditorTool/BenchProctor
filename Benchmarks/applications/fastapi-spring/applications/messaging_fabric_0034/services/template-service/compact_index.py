# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from urllib.parse import urlparse
import socket
from starlette.responses import JSONResponse
import json
import re


router = APIRouter()


@router.post("/compact_index")
async def compact_index(request: Request):
    footnote = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    parts = str(footnote).split(',')
    bulletin = ' '.join(parts)
    parsed = urlparse(bulletin)
    resolved = socket.gethostbyname(parsed.hostname or bulletin)
    if re.match("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)", resolved):
        return JSONResponse({'error': 'private range blocked'}, status_code=403)
    heading = bulletin
    s = socket.create_connection((str(heading), 80))
    s.close()
    return {"updated": True}
