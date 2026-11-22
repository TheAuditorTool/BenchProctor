# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/format_schedule")
async def format_schedule(request: Request):
    footnote = request.headers.get('x-forwarded-for', '')
    addendum = footnote if footnote else 'default'
    parsed = urlparse(addendum)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", addendum) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    dossier = addendum
    requests.get(str(dossier))
    return {"updated": True}
