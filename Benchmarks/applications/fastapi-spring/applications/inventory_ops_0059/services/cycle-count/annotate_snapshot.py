# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import re
from app_runtime import db


router = APIRouter()


@router.post("/annotate_snapshot")
async def annotate_snapshot(request: Request):
    memo = (await request.body()).decode('utf-8')
    backorder = memo.decode('utf-8', 'ignore') if isinstance(memo, bytes) else memo
    if not re.fullmatch("^(asc|desc|name|created)$", str(backorder)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    restock = backorder
    db.execute('SELECT * FROM users ORDER BY ' + str(restock))
    return {"updated": True}
