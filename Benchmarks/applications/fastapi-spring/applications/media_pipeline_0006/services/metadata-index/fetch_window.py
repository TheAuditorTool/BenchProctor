# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/fetch_window")
async def fetch_window(request: Request):
    passage = request.cookies.get('session_token', '')
    montage = bytes.fromhex(passage).decode('utf-8', 'ignore')
    if not re.fullmatch("^(asc|desc|name|created)$", str(montage)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    rendition = montage
    return HTMLResponse('<div>' + str(rendition) + '</div>')
