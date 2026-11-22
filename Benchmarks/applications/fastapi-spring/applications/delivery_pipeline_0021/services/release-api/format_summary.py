# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re
from app_runtime import redis_client


router = APIRouter()


@router.post("/format_summary")
async def format_summary(request: Request):
    summary = redis_client.get('user_data')
    kind = 'json' if str(summary).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            phrase = str(summary).strip()
        case _:
            phrase = str(summary)
    parsed = urlparse(phrase)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", phrase) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    subtitle = phrase
    requests.get(str(subtitle))
    return {"updated": True}
