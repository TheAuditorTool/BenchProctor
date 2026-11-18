# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from urllib.parse import unquote
from starlette.responses import JSONResponse
import re
from app_runtime import db


router = APIRouter()


@router.post("/normalize_alert")
async def normalize_alert(request: Request):
    caption = (await request.form()).get('field', '')
    gauge = unquote(caption)
    if not re.fullmatch("^(asc|desc|name|created)$", str(gauge)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    cohort = gauge
    db.execute('SELECT * FROM users ORDER BY ' + str(cohort))
    return {"updated": True}
