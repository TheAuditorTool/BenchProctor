# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/enrich_checkpoint")
async def enrich_checkpoint(request: Request):
    footnote = request.cookies.get('session_token', '')
    handshake = bytes.fromhex(footnote).decode('utf-8', 'ignore')
    if not re.fullmatch("^(asc|desc|name|created)$", str(handshake)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    blurb = handshake
    return HTMLResponse('<div>' + str(blurb) + '</div>')
