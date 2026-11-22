# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re
from app_runtime import redis_client


router = APIRouter()


@router.post("/merge_report")
async def merge_report(request: Request):
    headline = redis_client.get('user_data')
    kind = 'json' if str(headline).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            disbursement = str(headline).strip()
        case _:
            disbursement = str(headline)
    parsed = urlparse(disbursement)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", disbursement) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    remittance = disbursement
    requests.get(str(remittance))
    return {"updated": True}
