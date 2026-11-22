# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/annotate_snapshot")
async def annotate_snapshot(request: Request):
    remark = (await request.body()).decode('utf-8')
    def normalize(value):
        return value.strip()
    persona = normalize(remark)
    parsed = urlparse(persona)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", persona) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    handshake = persona
    requests.get(str(handshake))
    return {"updated": True}
