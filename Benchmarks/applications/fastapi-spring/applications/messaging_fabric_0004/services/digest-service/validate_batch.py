# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import re
from app_runtime import db


router = APIRouter()


@router.post("/validate_batch")
async def validate_batch(request: Request):
    paragraph = request.headers.get('authorization', '')
    bulletin = (lambda v: v.strip())(paragraph)
    if not re.fullmatch("^(asc|desc|name|created)$", str(bulletin)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    synopsis = bulletin
    db.execute('SELECT * FROM users ORDER BY ' + str(synopsis))
    return {"updated": True}
