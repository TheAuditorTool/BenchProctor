# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/load_receipt")
async def load_receipt(request: Request):
    heading = (await request.body()).decode('utf-8')
    handshake = heading.decode('utf-8', 'ignore') if isinstance(heading, bytes) else heading
    if not re.fullmatch("^(asc|desc|name|created)$", str(handshake)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    persona = handshake
    return HTMLResponse('<div>' + str(persona) + '</div>')
