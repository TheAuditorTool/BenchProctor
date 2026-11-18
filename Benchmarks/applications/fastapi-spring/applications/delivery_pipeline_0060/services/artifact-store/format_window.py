# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from urllib.parse import unquote
from starlette.responses import JSONResponse
import re
from app_runtime import db


router = APIRouter()


@router.post("/format_window")
async def format_window(request: Request):
    wording = (await request.form()).get('field', '')
    remark = unquote(wording)
    if not re.fullmatch("^(asc|desc|name|created)$", str(remark)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    phrase = remark
    db.execute('SELECT * FROM users ORDER BY ' + str(phrase))
    return {"updated": True}
