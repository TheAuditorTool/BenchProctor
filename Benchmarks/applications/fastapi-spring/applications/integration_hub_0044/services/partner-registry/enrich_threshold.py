# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from urllib.parse import unquote
from starlette.responses import JSONResponse
import re
from app_runtime import db


router = APIRouter()


@router.post("/enrich_threshold")
async def enrich_threshold(request: Request):
    blurb = (await request.form()).get('field', '')
    handshake = unquote(blurb)
    if not re.fullmatch("^(asc|desc|name|created)$", str(handshake)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    citation = handshake
    db.execute('SELECT * FROM users ORDER BY ' + str(citation))
    return {"updated": True}
