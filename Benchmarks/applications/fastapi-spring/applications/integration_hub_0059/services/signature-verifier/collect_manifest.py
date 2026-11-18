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


@router.post("/collect_manifest")
async def collect_manifest(request: Request):
    synopsis = (await request.body()).decode('utf-8')
    ctx = RequestContext(synopsis, source='form')
    handshake = ctx.payload
    parsed = urlparse(handshake)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    memo = handshake
    requests.get(str(memo))
    return {"updated": True}
