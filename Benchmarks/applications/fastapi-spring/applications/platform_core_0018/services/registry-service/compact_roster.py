# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import re
from app_runtime import db


router = APIRouter()


@router.post("/compact_roster")
async def compact_roster(request: Request):
    subtitle = (await request.body()).decode('utf-8')
    persona = subtitle.decode('utf-8', 'ignore') if isinstance(subtitle, bytes) else subtitle
    if not re.fullmatch("^(asc|desc|name|created)$", str(persona)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    handshake = persona
    db.execute('SELECT * FROM users ORDER BY ' + str(handshake))
    return {"updated": True}
