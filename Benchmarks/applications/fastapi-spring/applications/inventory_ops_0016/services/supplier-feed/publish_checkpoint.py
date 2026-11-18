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


@router.post("/publish_checkpoint")
async def publish_checkpoint(request: Request):
    citation = (await request.body()).decode('utf-8')
    ctx = RequestContext(citation, source='form')
    backorder = ctx.payload
    parsed = urlparse(backorder)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    restock = backorder
    requests.get(str(restock))
    return {"updated": True}
