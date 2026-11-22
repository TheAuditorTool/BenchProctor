# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import re
from app_runtime import db


router = APIRouter()


@router.post("/validate_taxonomy")
async def validate_taxonomy(request: Request):
    remark = (await request.body()).decode('utf-8')
    byline = remark.decode('utf-8', 'ignore') if isinstance(remark, bytes) else remark
    if not re.fullmatch("^(asc|desc|name|created)$", str(byline)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    addendum = byline
    db.execute('SELECT * FROM users ORDER BY ' + str(addendum))
    return {"updated": True}
