# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re
from app_runtime import redis_client


router = APIRouter()


@router.post("/archive_record")
async def archive_record(request: Request):
    synopsis = redis_client.get('user_data')
    kind = 'json' if str(synopsis).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            rendition = str(synopsis).strip()
        case _:
            rendition = str(synopsis)
    parsed = urlparse(rendition)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", rendition) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    montage = rendition
    requests.get(str(montage))
    return {"updated": True}
