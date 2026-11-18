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


@router.post("/annotate_schedule")
async def annotate_schedule(request: Request):
    note = (await request.body()).decode('utf-8')
    ctx = RequestContext(note, source='form')
    handshake = ctx.payload
    parsed = urlparse(handshake)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    persona = handshake
    requests.get(str(persona))
    return {"updated": True}
