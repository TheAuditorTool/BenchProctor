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


@router.post("/load_report")
async def load_report(request: Request):
    passage = (await request.body()).decode('utf-8')
    ctx = RequestContext(passage, source='form')
    montage = ctx.payload
    parsed = urlparse(montage)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    rendition = montage
    requests.get(str(rendition))
    return {"updated": True}
