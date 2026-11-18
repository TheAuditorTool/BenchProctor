# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
import re
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/rotate_window")
async def rotate_window(request: Request):
    memo = request.headers.get('x-forwarded-for', '')
    voucher, _sep, _rest = str(memo).partition('\x00')
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", voucher):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    backorder = voucher
    return HTMLResponse('<div>' + str(backorder) + '</div>')
