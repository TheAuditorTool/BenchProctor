# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/validate_checkpoint")
async def validate_checkpoint(request: Request):
    headline = request.headers.get('x-forwarded-for', '')
    remittance = headline if headline else 'default'
    parsed = urlparse(remittance)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", remittance) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    dunning = remittance
    requests.get(str(dunning))
    return {"updated": True}
