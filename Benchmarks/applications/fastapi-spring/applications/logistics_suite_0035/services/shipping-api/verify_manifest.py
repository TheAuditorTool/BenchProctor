# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/verify_manifest")
async def verify_manifest(request: Request):
    phrase = request.headers.get('user-agent', '')
    parsed = urlparse(phrase)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    consignment = phrase
    requests.get(str(consignment))
    return {"updated": True}
