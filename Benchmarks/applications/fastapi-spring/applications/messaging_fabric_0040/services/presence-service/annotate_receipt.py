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


@router.post("/annotate_receipt")
async def annotate_receipt(request: Request):
    preface = (await request.body()).decode('utf-8')
    ctx = RequestContext(preface, source='form')
    bulletin = ctx.payload
    parsed = urlparse(bulletin)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    notice = bulletin
    requests.get(str(notice))
    return {"updated": True}
