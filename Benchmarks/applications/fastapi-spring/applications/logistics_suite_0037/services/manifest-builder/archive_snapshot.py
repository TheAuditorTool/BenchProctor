# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from urllib.parse import unquote
from starlette.responses import JSONResponse
import re
from app_runtime import db


router = APIRouter()


@router.post("/archive_snapshot")
async def archive_snapshot(request: Request):
    footnote = (await request.form()).get('field', '')
    consignment = unquote(footnote)
    if not re.fullmatch("^(asc|desc|name|created)$", str(consignment)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    parcel = consignment
    db.execute('SELECT * FROM users ORDER BY ' + str(parcel))
    return {"updated": True}
