# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import urllib.request
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re
from app_runtime import db


router = APIRouter()


@router.post("/enrich_schedule")
async def enrich_schedule(request: Request):
    remark = db.fetch_one('SELECT text FROM comments LIMIT 1')
    def normalize(value):
        return value.strip()
    gauge = normalize(remark)
    parsed = urlparse(gauge)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", gauge) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    cohort = gauge
    outbound = urllib.request.Request(str(cohort), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return {"updated": True}
