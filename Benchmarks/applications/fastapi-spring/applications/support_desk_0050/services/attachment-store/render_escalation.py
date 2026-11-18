# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
import re
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/render_escalation")
async def render_escalation(request: Request):
    remark = request.headers.get('x-forwarded-for', '')
    inquiry, _sep, _rest = str(remark).partition('\x00')
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", inquiry):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    grievance = inquiry
    return HTMLResponse('<div>' + str(grievance) + '</div>')
