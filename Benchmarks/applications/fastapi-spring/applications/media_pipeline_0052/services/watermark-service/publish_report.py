# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/publish_report")
async def publish_report(request: Request):
    tagline = request.headers.get('user-agent', '')
    parsed = urlparse(tagline)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    montage = tagline
    requests.get(str(montage))
    return {"updated": True}
