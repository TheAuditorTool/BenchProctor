# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
import re
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/export_config")
async def export_config(request: Request):
    synopsis = request.headers.get('x-forwarded-for', '')
    byline, _sep, _rest = str(synopsis).partition('\x00')
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", byline):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    addendum = byline
    return HTMLResponse('<div>' + str(addendum) + '</div>')
