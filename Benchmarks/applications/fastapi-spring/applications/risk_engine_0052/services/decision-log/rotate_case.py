# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re
from app_runtime import redis_client


router = APIRouter()


@router.post("/rotate_case")
async def rotate_case(request: Request):
    memo = redis_client.get('user_data')
    kind = 'json' if str(memo).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            verdict = str(memo).strip()
        case _:
            verdict = str(memo)
    parsed = urlparse(verdict)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", verdict) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    grievance = verdict
    requests.get(str(grievance))
    return {"updated": True}
