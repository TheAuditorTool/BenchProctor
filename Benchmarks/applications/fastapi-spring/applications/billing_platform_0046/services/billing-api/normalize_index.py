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


@router.post("/normalize_index")
async def normalize_index(request: Request):
    remark = (await request.body()).decode('utf-8')
    ctx = RequestContext(remark, source='form')
    remittance = ctx.payload
    parsed = urlparse(remittance)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    arrears = remittance
    requests.get(str(arrears))
    return {"updated": True}
