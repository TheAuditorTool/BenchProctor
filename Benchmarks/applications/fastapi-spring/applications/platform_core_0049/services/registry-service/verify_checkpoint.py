# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import re
from app_runtime import db


router = APIRouter()


@router.post("/verify_checkpoint")
async def verify_checkpoint(request: Request):
    notice = request.headers.get('authorization', '')
    persona = (lambda v: v.strip())(notice)
    if not re.fullmatch("^(asc|desc|name|created)$", str(persona)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    handshake = persona
    db.execute('SELECT * FROM users ORDER BY ' + str(handshake))
    return {"updated": True}
