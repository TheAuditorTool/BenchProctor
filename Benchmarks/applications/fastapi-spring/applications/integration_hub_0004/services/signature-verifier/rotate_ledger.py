# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/rotate_ledger")
async def rotate_ledger(request: Request):
    summary = (await request.body()).decode('utf-8')
    handshake = summary.decode('utf-8', 'ignore') if isinstance(summary, bytes) else summary
    if not re.fullmatch("^(asc|desc|name|created)$", str(handshake)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    paragraph = handshake
    return HTMLResponse('<div>' + str(paragraph) + '</div>')
