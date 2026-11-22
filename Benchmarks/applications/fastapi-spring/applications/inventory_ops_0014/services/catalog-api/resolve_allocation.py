# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re
from app_runtime import redis_client


router = APIRouter()


@router.post("/resolve_allocation")
async def resolve_allocation(request: Request):
    excerpt = redis_client.get('user_data')
    kind = 'json' if str(excerpt).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            restock = str(excerpt).strip()
        case _:
            restock = str(excerpt)
    parsed = urlparse(restock)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", restock) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    backorder = restock
    requests.get(str(backorder))
    return {"updated": True}
