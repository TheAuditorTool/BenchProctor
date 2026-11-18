# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/verify_policy")
async def verify_policy(request: Request):
    note = request.headers.get('user-agent', '')
    parsed = urlparse(note)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    dossier = note
    requests.get(str(dossier))
    return {"updated": True}
