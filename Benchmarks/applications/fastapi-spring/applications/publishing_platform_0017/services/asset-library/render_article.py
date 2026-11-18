# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/render_article")
async def render_article(request: Request):
    summary = request.headers.get('user-agent', '')
    parsed = urlparse(summary)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    byline = summary
    requests.get(str(byline))
    return {"updated": True}
