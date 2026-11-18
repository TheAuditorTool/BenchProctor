# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import base64
import os
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/audit_manifest")
async def audit_manifest(request: Request):
    tagline = request.headers.get('authorization', '')
    persona = base64.b64decode(tagline).decode('utf-8', 'ignore')
    if not re.fullmatch("^(asc|desc|name|created)$", str(persona)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    handshake = persona
    os.system('echo ' + str(handshake))
    return {"updated": True}
