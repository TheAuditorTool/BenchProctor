# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/prune_checkpoint")
async def prune_checkpoint(request: Request):
    note = request.headers.get('user-agent', '')
    parsed = urlparse(note)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    cohort = note
    requests.get(str(cohort))
    return {"updated": True}
