# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/format_record")
async def format_record(request: Request):
    caption = request.headers.get('x-forwarded-for', '')
    handshake = caption if caption else 'default'
    parsed = urlparse(handshake)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", handshake) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    subject = handshake
    requests.get(str(subject))
    return {"updated": True}
