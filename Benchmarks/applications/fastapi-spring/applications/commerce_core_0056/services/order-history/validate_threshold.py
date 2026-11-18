# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from urllib.parse import unquote
from starlette.responses import JSONResponse
import re
from app_runtime import db


router = APIRouter()


@router.post("/validate_threshold")
async def validate_threshold(request: Request):
    citation = (await request.form()).get('field', '')
    backorder = unquote(citation)
    if not re.fullmatch("^(asc|desc|name|created)$", str(backorder)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    voucher = backorder
    db.execute('SELECT * FROM users ORDER BY ' + str(voucher))
    return {"updated": True}
