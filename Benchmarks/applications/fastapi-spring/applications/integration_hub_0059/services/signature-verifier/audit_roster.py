# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from urllib.parse import unquote
from starlette.responses import JSONResponse
import re
from app_runtime import db


router = APIRouter()


@router.post("/audit_roster")
async def audit_roster(request: Request):
    synopsis = (await request.form()).get('field', '')
    handshake = unquote(synopsis)
    if not re.fullmatch("^(asc|desc|name|created)$", str(handshake)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    memo = handshake
    db.execute('SELECT * FROM users ORDER BY ' + str(memo))
    return {"updated": True}
