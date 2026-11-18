# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/audit_header")
async def audit_header(request: Request):
    summary = request.cookies.get('session_token', '')
    addendum = bytes.fromhex(summary).decode('utf-8', 'ignore')
    if not re.fullmatch("^(asc|desc|name|created)$", str(addendum)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    byline = addendum
    return HTMLResponse('<div>' + str(byline) + '</div>')
