# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import base64
import os
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/resolve_window")
async def resolve_window(request: Request):
    blurb = request.headers.get('authorization', '')
    handshake = base64.b64decode(blurb).decode('utf-8', 'ignore')
    if not re.fullmatch("^(asc|desc|name|created)$", str(handshake)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    citation = handshake
    os.system('echo ' + str(citation))
    return {"updated": True}
