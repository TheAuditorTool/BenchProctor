# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from urllib.parse import unquote
from starlette.responses import JSONResponse
import re
from app_runtime import db


router = APIRouter()


@router.post("/fetch_record")
async def fetch_record(request: Request):
    preface = (await request.form()).get('field', '')
    bulletin = unquote(preface)
    if not re.fullmatch("^(asc|desc|name|created)$", str(bulletin)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    notice = bulletin
    db.execute('SELECT * FROM users ORDER BY ' + str(notice))
    return {"updated": True}
