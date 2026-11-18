# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/enrich_mapping")
async def enrich_mapping(request: Request):
    synopsis = request.headers.get('user-agent', '')
    parsed = urlparse(synopsis)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    memo = synopsis
    requests.get(str(memo))
    return {"updated": True}
