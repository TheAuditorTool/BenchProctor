# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import re
from app_runtime import db


router = APIRouter()


@router.post("/format_header")
async def format_header(request: Request):
    blurb = (await request.body()).decode('utf-8')
    inquiry = blurb.decode('utf-8', 'ignore') if isinstance(blurb, bytes) else blurb
    if not re.fullmatch("^(asc|desc|name|created)$", str(inquiry)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    grievance = inquiry
    db.execute('SELECT * FROM users ORDER BY ' + str(grievance))
    return {"updated": True}
