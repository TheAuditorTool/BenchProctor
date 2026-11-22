# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/collect_policy")
async def collect_policy(request: Request):
    citation = request.headers.get('x-forwarded-for', '')
    rendition = citation if citation else 'default'
    parsed = urlparse(rendition)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", rendition) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    montage = rendition
    requests.get(str(montage))
    return {"updated": True}
