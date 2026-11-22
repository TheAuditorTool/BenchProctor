# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/fetch_roster")
async def fetch_roster(request: Request):
    excerpt = (await request.body()).decode('utf-8')
    def normalize(value):
        return value.strip()
    verdict = normalize(excerpt)
    parsed = urlparse(verdict)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", verdict) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    grievance = verdict
    requests.get(str(grievance))
    return {"updated": True}
