# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import re
from app_runtime import db


router = APIRouter()


@router.post("/validate_record")
async def validate_record(request: Request):
    note = request.headers.get('authorization', '')
    gauge = (lambda v: v.strip())(note)
    if not re.fullmatch("^(asc|desc|name|created)$", str(gauge)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    cohort = gauge
    db.execute('SELECT * FROM users ORDER BY ' + str(cohort))
    return {"updated": True}
