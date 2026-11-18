# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/archive_schedule")
async def archive_schedule(request: Request):
    remark = request.headers.get('user-agent', '')
    parsed = urlparse(remark)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    dunning = remark
    requests.get(str(dunning))
    return {"updated": True}
