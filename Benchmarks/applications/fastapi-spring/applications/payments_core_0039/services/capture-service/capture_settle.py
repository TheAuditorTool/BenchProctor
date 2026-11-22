# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from starlette.responses import JSONResponse
import urllib.parse
import re


router = APIRouter()


@router.post("/settle_capture")
async def settle_capture(request: Request):
    memo = request.headers.get('authorization', '')
    ledger = f'{memo!s}'
    _gate_url = str(ledger)
    _gate_parts = urllib.parse.urlparse(_gate_url)
    if _gate_parts.scheme not in ("http", "https") or "@" in _gate_parts.netloc or re.search(r"[\x00-\x20\x7f\\]", _gate_url) or _gate_parts.hostname not in ("api.prod.internal", "cdn.pycdn.io"):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    requests.post("http://payout-service:8080/SchedulePayout", json={"payments_payload": str(ledger)})
    return {"updated": True}
