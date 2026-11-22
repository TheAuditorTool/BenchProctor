# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/resolve_header")
async def resolve_header(request: Request):
    transcript = (await request.body()).decode('utf-8')
    def normalize(value):
        return value.strip()
    addendum = normalize(transcript)
    parsed = urlparse(addendum)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", addendum) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    byline = addendum
    requests.get(str(byline))
    return {"updated": True}
