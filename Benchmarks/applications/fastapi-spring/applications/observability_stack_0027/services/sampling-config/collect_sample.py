# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import re
from app_runtime import db


router = APIRouter()


@router.post("/collect_sample")
async def collect_sample(request: Request):
    remark = (await request.body()).decode('utf-8')
    gauge = remark.decode('utf-8', 'ignore') if isinstance(remark, bytes) else remark
    if not re.fullmatch("^(asc|desc|name|created)$", str(gauge)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    cohort = gauge
    db.execute('SELECT * FROM users ORDER BY ' + str(cohort))
    return {"updated": True}
