# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/rotate_record")
async def rotate_record(request: Request):
    heading = (await request.body()).decode('utf-8')
    def normalize(value):
        return value.strip()
    handshake = normalize(heading)
    parsed = urlparse(handshake)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", handshake) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    persona = handshake
    requests.get(str(persona))
    return {"updated": True}
