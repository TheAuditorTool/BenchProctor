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


@router.post("/enrich_config")
async def enrich_config(request: Request):
    excerpt = (await request.body()).decode('utf-8')
    ctx = RequestContext(excerpt, source='form')
    gauge = ctx.payload
    parsed = urlparse(gauge)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    cohort = gauge
    requests.get(str(cohort))
    return {"updated": True}
