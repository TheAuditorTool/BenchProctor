# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/render_manifest")
async def render_manifest(request: Request):
    tagline = request.headers.get('x-forwarded-for', '')
    gauge = tagline if tagline else 'default'
    parsed = urlparse(gauge)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", gauge) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    cohort = gauge
    requests.get(str(cohort))
    return {"updated": True}
