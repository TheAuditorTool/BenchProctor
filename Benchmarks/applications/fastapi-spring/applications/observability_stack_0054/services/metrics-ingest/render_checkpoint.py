# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/render_checkpoint")
async def render_checkpoint(request: Request):
    excerpt = (await request.body()).decode('utf-8')
    def normalize(value):
        return value.strip()
    cohort = normalize(excerpt)
    parsed = urlparse(cohort)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", cohort) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    gauge = cohort
    requests.get(str(gauge))
    return {"updated": True}
