# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/audit_batch")
async def audit_batch(request: Request):
    note = request.cookies.get('session_token', '')
    addendum = bytes.fromhex(note).decode('utf-8', 'ignore')
    if not re.fullmatch("^(asc|desc|name|created)$", str(addendum)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    dossier = addendum
    return HTMLResponse('<div>' + str(dossier) + '</div>')
