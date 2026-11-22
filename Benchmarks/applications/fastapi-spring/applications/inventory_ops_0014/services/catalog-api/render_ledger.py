# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/render_ledger")
async def render_ledger(request: Request):
    excerpt = (await request.body()).decode('utf-8')
    restock = ' '.join(str(excerpt).split())
    parsed = urlparse(restock)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", restock) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    backorder = restock
    requests.get(str(backorder))
    return {"updated": True}
