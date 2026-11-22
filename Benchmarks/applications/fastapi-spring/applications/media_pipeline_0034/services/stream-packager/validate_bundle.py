# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/validate_bundle")
async def validate_bundle(request: Request):
    synopsis = (await request.body()).decode('utf-8')
    def normalize(value):
        return value.strip()
    rendition = normalize(synopsis)
    parsed = urlparse(rendition)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", rendition) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    montage = rendition
    requests.get(str(montage))
    return {"updated": True}
