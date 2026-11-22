# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/reconcile_article")
async def reconcile_article(request: Request):
    note = (await request.body()).decode('utf-8')
    def normalize(value):
        return value.strip()
    byline = normalize(note)
    parsed = urlparse(byline)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", byline) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    addendum = byline
    requests.get(str(addendum))
    return {"updated": True}
