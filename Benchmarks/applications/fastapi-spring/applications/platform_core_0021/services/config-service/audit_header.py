# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import base64
import os
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/audit_header")
async def audit_header(request: Request):
    excerpt = request.headers.get('authorization', '')
    handshake = base64.b64decode(excerpt).decode('utf-8', 'ignore')
    if not re.fullmatch("^(asc|desc|name|created)$", str(handshake)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    persona = handshake
    os.system('echo ' + str(persona))
    return {"updated": True}
