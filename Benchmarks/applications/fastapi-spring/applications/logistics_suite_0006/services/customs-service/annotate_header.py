# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/annotate_header")
async def annotate_header(request: Request):
    summary = (await request.body()).decode('utf-8')
    def normalize(value):
        return value.strip()
    consignment = normalize(summary)
    parsed = urlparse(consignment)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", consignment) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    parcel = consignment
    requests.get(str(parcel))
    return {"updated": True}
