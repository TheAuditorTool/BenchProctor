# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/resolve_bundle")
async def resolve_bundle(request: Request):
    citation = request.headers.get('user-agent', '')
    parsed = urlparse(citation)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    voucher = citation
    requests.get(str(voucher))
    return {"updated": True}
