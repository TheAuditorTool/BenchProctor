# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import re
from app_runtime import db


router = APIRouter()


@router.post("/archive_index")
async def archive_index(request: Request):
    synopsis = request.headers.get('authorization', '')
    arrears = (lambda v: v.strip())(synopsis)
    if not re.fullmatch("^(asc|desc|name|created)$", str(arrears)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    dunning = arrears
    db.execute('SELECT * FROM users ORDER BY ' + str(dunning))
    return {"updated": True}
