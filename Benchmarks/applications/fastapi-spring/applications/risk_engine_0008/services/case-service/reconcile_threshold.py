# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/reconcile_threshold")
async def reconcile_threshold(request: Request):
    synopsis = request.cookies.get('session_token', '')
    verdict = bytes.fromhex(synopsis).decode('utf-8', 'ignore')
    if not re.fullmatch("^(asc|desc|name|created)$", str(verdict)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    grievance = verdict
    return HTMLResponse('<div>' + str(grievance) + '</div>')
