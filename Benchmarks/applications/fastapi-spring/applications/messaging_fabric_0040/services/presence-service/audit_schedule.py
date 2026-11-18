# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/audit_schedule")
async def audit_schedule(request: Request):
    preface = request.cookies.get('session_token', '')
    bulletin = bytes.fromhex(preface).decode('utf-8', 'ignore')
    if not re.fullmatch("^(asc|desc|name|created)$", str(bulletin)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    notice = bulletin
    return HTMLResponse('<div>' + str(notice) + '</div>')
