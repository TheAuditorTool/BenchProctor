# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
import re
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/rotate_batch")
async def rotate_batch(request: Request):
    notice = request.headers.get('x-forwarded-for', '')
    persona, _sep, _rest = str(notice).partition('\x00')
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", persona):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    handshake = persona
    return HTMLResponse('<div>' + str(handshake) + '</div>')
