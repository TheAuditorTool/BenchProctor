# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import urllib.request
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/archive_policy")
async def archive_policy(request: Request):
    caption = request.headers.get('authorization', '')
    handshake = caption if caption else 'default'
    parsed = urlparse(handshake)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", handshake) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    subject = handshake
    outbound = urllib.request.Request(str(subject), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return {"updated": True}
