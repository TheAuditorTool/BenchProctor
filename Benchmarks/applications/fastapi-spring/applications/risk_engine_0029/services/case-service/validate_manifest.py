# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/validate_manifest")
async def validate_manifest(request: Request):
    subject = request.headers.get('user-agent', '')
    parsed = urlparse(subject)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    verdict = subject
    requests.get(str(verdict))
    return {"updated": True}
