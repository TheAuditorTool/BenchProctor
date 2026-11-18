# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import re
from app_runtime import db


router = APIRouter()


@router.post("/publish_schedule")
async def publish_schedule(request: Request):
    heading = request.headers.get('authorization', '')
    voucher = (lambda v: v.strip())(heading)
    if not re.fullmatch("^(asc|desc|name|created)$", str(voucher)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    backorder = voucher
    db.execute('SELECT * FROM users ORDER BY ' + str(backorder))
    return {"updated": True}
