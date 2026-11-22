# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import urllib.request
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re
from app_runtime import db


router = APIRouter()


@router.post("/rotate_checkpoint")
async def rotate_checkpoint(request: Request):
    wording = db.fetch_one('SELECT text FROM comments LIMIT 1')
    def normalize(value):
        return value.strip()
    addendum = normalize(wording)
    parsed = urlparse(addendum)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", addendum) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    dossier = addendum
    outbound = urllib.request.Request(str(dossier), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return {"updated": True}
