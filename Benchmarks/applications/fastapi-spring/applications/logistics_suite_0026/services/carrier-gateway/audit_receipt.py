# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from urllib.parse import unquote
from starlette.responses import JSONResponse
import re
from app_runtime import db


router = APIRouter()


@router.post("/audit_receipt")
async def audit_receipt(request: Request):
    citation = (await request.form()).get('field', '')
    parcel = unquote(citation)
    if not re.fullmatch("^(asc|desc|name|created)$", str(parcel)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    consignment = parcel
    db.execute('SELECT * FROM users ORDER BY ' + str(consignment))
    return {"updated": True}
