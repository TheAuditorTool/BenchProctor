# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
import re
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/fetch_roster")
async def fetch_roster(request: Request):
    snippet = request.headers.get('x-forwarded-for', '')
    persona, _sep, _rest = str(snippet).partition('\x00')
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", persona):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    synopsis = persona
    return HTMLResponse('<div>' + str(synopsis) + '</div>')
