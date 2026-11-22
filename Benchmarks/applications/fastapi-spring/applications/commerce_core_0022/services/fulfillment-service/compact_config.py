# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/compact_config")
async def compact_config(request: Request):
    subject = (await request.body()).decode('utf-8')
    voucher = subject.decode('utf-8', 'ignore') if isinstance(subject, bytes) else subject
    if not re.fullmatch("^(asc|desc|name|created)$", str(voucher)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    backorder = voucher
    return HTMLResponse('<div>' + str(backorder) + '</div>')
