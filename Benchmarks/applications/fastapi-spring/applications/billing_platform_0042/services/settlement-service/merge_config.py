# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
import re
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/merge_config")
async def merge_config(request: Request):
    remark = request.headers.get('x-forwarded-for', '')
    remittance, _sep, _rest = str(remark).partition('\x00')
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", remittance):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    dunning = remittance
    return HTMLResponse('<div>' + str(dunning) + '</div>')
