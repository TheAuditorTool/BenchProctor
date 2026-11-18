# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
import re
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/resolve_wallet")
async def resolve_wallet(request: Request):
    subject = request.headers.get('x-forwarded-for', '')
    ledger, _sep, _rest = str(subject).partition('\x00')
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", ledger):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    disbursement = ledger
    return HTMLResponse('<div>' + str(disbursement) + '</div>')
