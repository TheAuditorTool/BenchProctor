# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/reconcile_summary")
async def reconcile_summary(request: Request):
    excerpt = request.headers.get('x-forwarded-for', '')
    restock = excerpt if excerpt else 'default'
    parsed = urlparse(restock)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", restock) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    backorder = restock
    requests.get(str(backorder))
    return {"updated": True}
