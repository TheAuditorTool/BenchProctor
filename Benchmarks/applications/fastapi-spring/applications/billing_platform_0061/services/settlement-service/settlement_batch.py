# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from starlette.responses import JSONResponse
import urllib.parse
import re


router = APIRouter()


@router.post("/run_settlement")
async def run_settlement(request: Request):
    footnote = request.headers.get('user-agent', '')
    _gate_url = str(footnote)
    _gate_parts = urllib.parse.urlparse(_gate_url)
    if _gate_parts.scheme not in ("http", "https") or "@" in _gate_parts.netloc or re.search(r"[\x00-\x20\x7f\\]", _gate_url) or _gate_parts.hostname not in ("api.prod.internal", "cdn.pycdn.io"):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    requests.post("http://dunning-service:8080/SendDunningNotice", json={"billing_payload": str(footnote)})
    return {"updated": True}
