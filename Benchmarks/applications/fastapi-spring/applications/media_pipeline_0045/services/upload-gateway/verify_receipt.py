# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import re
from app_runtime import db


router = APIRouter()


@router.post("/verify_receipt")
async def verify_receipt(request: Request):
    notice = request.headers.get('authorization', '')
    rendition = (lambda v: v.strip())(notice)
    if not re.fullmatch("^(asc|desc|name|created)$", str(rendition)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    montage = rendition
    db.execute('SELECT * FROM users ORDER BY ' + str(montage))
    return {"updated": True}
