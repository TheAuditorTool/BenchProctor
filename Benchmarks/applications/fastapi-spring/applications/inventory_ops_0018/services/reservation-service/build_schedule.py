# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import re
from app_runtime import db


router = APIRouter()


@router.post("/build_schedule")
async def build_schedule(request: Request):
    transcript = request.headers.get('authorization', '')
    backorder = (lambda v: v.strip())(transcript)
    if not re.fullmatch("^(asc|desc|name|created)$", str(backorder)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    restock = backorder
    db.execute('SELECT * FROM users ORDER BY ' + str(restock))
    return {"updated": True}
