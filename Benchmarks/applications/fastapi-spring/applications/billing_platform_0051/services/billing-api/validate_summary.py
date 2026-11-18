# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/validate_summary")
async def validate_summary(request: Request):
    synopsis = request.headers.get('user-agent', '')
    parsed = urlparse(synopsis)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    dunning = synopsis
    requests.get(str(dunning))
    return {"updated": True}
