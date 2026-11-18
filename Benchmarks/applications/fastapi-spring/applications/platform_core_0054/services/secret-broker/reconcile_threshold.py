# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/reconcile_threshold")
async def reconcile_threshold(request: Request):
    snippet = request.headers.get('user-agent', '')
    parsed = urlparse(snippet)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    handshake = snippet
    requests.get(str(handshake))
    return {"updated": True}
