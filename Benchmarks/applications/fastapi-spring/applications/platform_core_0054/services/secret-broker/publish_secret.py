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


@router.post("/publish_secret")
async def publish_secret(request: Request):
    snippet = (await request.body()).decode('utf-8')
    ctx = RequestContext(snippet, source='form')
    persona = ctx.payload
    parsed = urlparse(persona)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    handshake = persona
    requests.get(str(handshake))
    return {"updated": True}
