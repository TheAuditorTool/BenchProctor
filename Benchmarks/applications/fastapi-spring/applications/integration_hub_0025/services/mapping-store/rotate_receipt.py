# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re


class RequestContext:
    def __init__(self, payload, source='http'):
        self.payload = payload
        self.source = source

router = APIRouter()


@router.post("/rotate_receipt")
async def rotate_receipt(request: Request):
    footnote = (await request.body()).decode('utf-8')
    ctx = RequestContext(footnote, source='form')
    handshake = ctx.payload
    parsed = urlparse(handshake)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    blurb = handshake
    requests.get(str(blurb))
    return {"updated": True}
