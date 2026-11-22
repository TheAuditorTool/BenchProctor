# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import urllib.request
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/validate_manifest")
async def validate_manifest(request: Request):
    subject = request.headers.get('authorization', '')
    voucher = subject if subject else 'default'
    parsed = urlparse(voucher)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", voucher) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    backorder = voucher
    outbound = urllib.request.Request(str(backorder), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return {"updated": True}
