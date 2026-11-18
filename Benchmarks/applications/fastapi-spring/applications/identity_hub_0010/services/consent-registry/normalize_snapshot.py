# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from urllib.parse import unquote
from starlette.responses import JSONResponse
import re
from app_runtime import db


router = APIRouter()


@router.post("/normalize_snapshot")
async def normalize_snapshot(request: Request):
    phrase = (await request.form()).get('field', '')
    persona = unquote(phrase)
    if not re.fullmatch("^(asc|desc|name|created)$", str(persona)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    transcript = persona
    db.execute('SELECT * FROM users ORDER BY ' + str(transcript))
    return {"updated": True}
