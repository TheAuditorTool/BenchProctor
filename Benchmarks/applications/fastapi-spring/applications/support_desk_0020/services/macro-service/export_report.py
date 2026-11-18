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


@router.post("/export_report")
async def export_report(request: Request):
    phrase = (await request.body()).decode('utf-8')
    ctx = RequestContext(phrase, source='form')
    inquiry = ctx.payload
    parsed = urlparse(inquiry)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    grievance = inquiry
    requests.get(str(grievance))
    return {"updated": True}
