# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/build_threshold")
async def build_threshold(request: Request):
    citation = request.headers.get('user-agent', '')
    parsed = urlparse(citation)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    consignment = citation
    requests.get(str(consignment))
    return {"updated": True}
