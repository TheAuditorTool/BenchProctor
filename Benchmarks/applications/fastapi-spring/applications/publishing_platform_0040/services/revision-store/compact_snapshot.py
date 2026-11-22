# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re
from app_runtime import redis_client


router = APIRouter()


@router.post("/compact_snapshot")
async def compact_snapshot(request: Request):
    transcript = redis_client.get('user_data')
    kind = 'json' if str(transcript).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            addendum = str(transcript).strip()
        case _:
            addendum = str(transcript)
    parsed = urlparse(addendum)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", addendum) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    byline = addendum
    requests.get(str(byline))
    return {"updated": True}
