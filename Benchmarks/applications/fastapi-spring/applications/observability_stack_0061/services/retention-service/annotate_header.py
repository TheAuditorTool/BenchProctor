# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/annotate_header")
async def annotate_header(request: Request):
    headline = request.headers.get('user-agent', '')
    parsed = urlparse(headline)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    gauge = headline
    requests.get(str(gauge))
    return {"updated": True}
