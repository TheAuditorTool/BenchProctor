# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/load_policy")
async def load_policy(request: Request):
    citation = request.headers.get('x-forwarded-for', '')
    parcel = citation if citation else 'default'
    parsed = urlparse(parcel)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", parcel) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    consignment = parcel
    requests.get(str(consignment))
    return {"updated": True}
