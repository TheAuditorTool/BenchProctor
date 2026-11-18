# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from urllib.parse import unquote
from starlette.responses import JSONResponse
import re
from app_runtime import db


router = APIRouter()


@router.post("/compact_secret")
async def compact_secret(request: Request):
    snippet = (await request.form()).get('field', '')
    persona = unquote(snippet)
    if not re.fullmatch("^(asc|desc|name|created)$", str(persona)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    handshake = persona
    db.execute('SELECT * FROM users ORDER BY ' + str(handshake))
    return {"updated": True}
