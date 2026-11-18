# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/build_report")
async def build_report(request: Request):
    summary = request.cookies.get('session_token', '')
    restock = bytes.fromhex(summary).decode('utf-8', 'ignore')
    if not re.fullmatch("^(asc|desc|name|created)$", str(restock)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    backorder = restock
    return HTMLResponse('<div>' + str(backorder) + '</div>')
