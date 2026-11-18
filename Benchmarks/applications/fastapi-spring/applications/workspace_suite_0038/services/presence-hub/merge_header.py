# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from urllib.parse import unquote
from starlette.responses import JSONResponse
import re
from app_runtime import db


router = APIRouter()


@router.post("/merge_header")
async def merge_header(request: Request):
    preface = (await request.form()).get('field', '')
    remark = unquote(preface)
    if not re.fullmatch("^(asc|desc|name|created)$", str(remark)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    wording = remark
    db.execute('SELECT * FROM users ORDER BY ' + str(wording))
    return {"updated": True}
