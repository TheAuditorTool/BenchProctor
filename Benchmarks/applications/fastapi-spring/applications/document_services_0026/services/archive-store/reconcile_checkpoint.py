# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import urllib.request
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/reconcile_checkpoint")
async def reconcile_checkpoint(request: Request):
    preface = request.headers.get('authorization', '')
    addendum = preface if preface else 'default'
    parsed = urlparse(addendum)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", addendum) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    dossier = addendum
    outbound = urllib.request.Request(str(dossier), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return {"updated": True}
