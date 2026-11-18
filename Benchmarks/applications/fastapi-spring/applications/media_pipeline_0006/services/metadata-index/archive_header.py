# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/archive_header")
async def archive_header(request: Request):
    passage = request.headers.get('user-agent', '')
    parsed = urlparse(passage)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    rendition = passage
    requests.get(str(rendition))
    return {"updated": True}
