# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/build_checkpoint")
async def build_checkpoint(request: Request):
    memo = request.headers.get('user-agent', '')
    parsed = urlparse(memo)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    backorder = memo
    requests.get(str(backorder))
    return {"updated": True}
