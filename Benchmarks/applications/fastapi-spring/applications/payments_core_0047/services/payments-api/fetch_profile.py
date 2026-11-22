# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re
from app_runtime import redis_client


router = APIRouter()


@router.post("/fetch_profile")
async def fetch_profile(request: Request):
    footnote = redis_client.get('user_data')
    kind = 'json' if str(footnote).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            remittance = str(footnote).strip()
        case _:
            remittance = str(footnote)
    parsed = urlparse(remittance)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", remittance) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    disbursement = remittance
    requests.get(str(disbursement))
    return {"updated": True}
