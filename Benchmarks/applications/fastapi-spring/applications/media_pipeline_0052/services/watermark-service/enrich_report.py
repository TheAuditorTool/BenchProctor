# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/enrich_report")
async def enrich_report(request: Request):
    tagline = request.cookies.get('session_token', '')
    rendition = bytes.fromhex(tagline).decode('utf-8', 'ignore')
    if not re.fullmatch("^(asc|desc|name|created)$", str(rendition)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    montage = rendition
    return HTMLResponse('<div>' + str(montage) + '</div>')
