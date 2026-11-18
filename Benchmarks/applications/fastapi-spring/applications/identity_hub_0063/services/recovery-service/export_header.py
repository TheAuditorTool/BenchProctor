# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/export_header")
async def export_header(request: Request):
    paragraph = request.cookies.get('session_token', '')
    persona = bytes.fromhex(paragraph).decode('utf-8', 'ignore')
    if not re.fullmatch("^(asc|desc|name|created)$", str(persona)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    synopsis = persona
    return HTMLResponse('<div>' + str(synopsis) + '</div>')
