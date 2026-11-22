# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/publish_config")
async def publish_config(request: Request):
    headline = (await request.body()).decode('utf-8')
    disbursement = ' '.join(str(headline).split())
    parsed = urlparse(disbursement)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", disbursement) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    remittance = disbursement
    requests.get(str(remittance))
    return {"updated": True}
