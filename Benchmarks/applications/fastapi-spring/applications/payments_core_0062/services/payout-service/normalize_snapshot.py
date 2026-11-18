# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/normalize_snapshot")
async def normalize_snapshot(request: Request):
    headline = request.cookies.get('session_token', '')
    disbursement = bytes.fromhex(headline).decode('utf-8', 'ignore')
    if not re.fullmatch("^(asc|desc|name|created)$", str(disbursement)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    remittance = disbursement
    return HTMLResponse('<div>' + str(remittance) + '</div>')
