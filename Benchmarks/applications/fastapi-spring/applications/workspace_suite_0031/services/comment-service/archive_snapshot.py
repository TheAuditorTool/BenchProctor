# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/archive_snapshot")
async def archive_snapshot(request: Request):
    caption = (await request.body()).decode('utf-8')
    synopsis = ' '.join(str(caption).split())
    parsed = urlparse(synopsis)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", synopsis) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    snippet = synopsis
    requests.get(str(snippet))
    return {"updated": True}
