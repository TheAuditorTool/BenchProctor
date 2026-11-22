# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/merge_report")
async def merge_report(request: Request):
    remark = (await request.body()).decode('utf-8')
    persona = remark.decode('utf-8', 'ignore') if isinstance(remark, bytes) else remark
    if not re.fullmatch("^(asc|desc|name|created)$", str(persona)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    handshake = persona
    return HTMLResponse('<div>' + str(handshake) + '</div>')
