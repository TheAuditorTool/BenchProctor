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


@router.post("/merge_bundle")
async def merge_bundle(request: Request):
    subject = (await request.body()).decode('utf-8')
    ctx = RequestContext(subject, source='form')
    ledger = ctx.payload
    parsed = urlparse(ledger)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    disbursement = ledger
    requests.get(str(disbursement))
    return {"updated": True}
