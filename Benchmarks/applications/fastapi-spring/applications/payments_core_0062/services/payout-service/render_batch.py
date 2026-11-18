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


@router.post("/render_batch")
async def render_batch(request: Request):
    headline = (await request.body()).decode('utf-8')
    ctx = RequestContext(headline, source='form')
    disbursement = ctx.payload
    parsed = urlparse(disbursement)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    remittance = disbursement
    requests.get(str(remittance))
    return {"updated": True}
