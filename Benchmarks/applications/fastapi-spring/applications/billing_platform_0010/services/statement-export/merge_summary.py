# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/merge_summary")
async def merge_summary(request: Request):
    headline = (await request.body()).decode('utf-8')
    remittance = ' '.join(str(headline).split())
    parsed = urlparse(remittance)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", remittance) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    dunning = remittance
    requests.get(str(dunning))
    return {"updated": True}
