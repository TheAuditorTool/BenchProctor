# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/normalize_roster")
async def normalize_roster(request: Request):
    passage = request.headers.get('user-agent', '')
    parsed = urlparse(passage)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    handshake = passage
    requests.get(str(handshake))
    return {"updated": True}
