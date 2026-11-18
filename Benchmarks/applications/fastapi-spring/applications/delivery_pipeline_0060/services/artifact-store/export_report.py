# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/export_report")
async def export_report(request: Request):
    wording = request.cookies.get('session_token', '')
    remark = bytes.fromhex(wording).decode('utf-8', 'ignore')
    if not re.fullmatch("^(asc|desc|name|created)$", str(remark)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    phrase = remark
    return HTMLResponse('<div>' + str(phrase) + '</div>')
