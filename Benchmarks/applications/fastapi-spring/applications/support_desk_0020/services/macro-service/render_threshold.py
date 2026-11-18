# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/render_threshold")
async def render_threshold(request: Request):
    phrase = request.cookies.get('session_token', '')
    inquiry = bytes.fromhex(phrase).decode('utf-8', 'ignore')
    if not re.fullmatch("^(asc|desc|name|created)$", str(inquiry)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    grievance = inquiry
    return HTMLResponse('<div>' + str(grievance) + '</div>')
