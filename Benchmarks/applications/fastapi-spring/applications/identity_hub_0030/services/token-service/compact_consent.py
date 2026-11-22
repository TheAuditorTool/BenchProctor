# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re
from app_runtime import redis_client


router = APIRouter()


@router.post("/compact_consent")
async def compact_consent(request: Request):
    tagline = redis_client.get('user_data')
    kind = 'json' if str(tagline).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            persona = str(tagline).strip()
        case _:
            persona = str(tagline)
    parsed = urlparse(persona)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", persona) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    note = persona
    requests.get(str(note))
    return {"updated": True}
