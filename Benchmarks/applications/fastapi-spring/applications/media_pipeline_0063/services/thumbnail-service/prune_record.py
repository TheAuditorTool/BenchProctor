# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re
from app_runtime import redis_client


router = APIRouter()


@router.post("/prune_record")
async def prune_record(request: Request):
    snippet = redis_client.get('user_data')
    kind = 'json' if str(snippet).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            montage = str(snippet).strip()
        case _:
            montage = str(snippet)
    parsed = urlparse(montage)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", montage) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    rendition = montage
    requests.get(str(rendition))
    return {"updated": True}
