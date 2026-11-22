# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import re
from app_runtime import db


router = APIRouter()


@router.post("/prune_checkpoint")
async def prune_checkpoint(request: Request):
    quotation = (await request.body()).decode('utf-8')
    parcel = quotation.decode('utf-8', 'ignore') if isinstance(quotation, bytes) else quotation
    if not re.fullmatch("^(asc|desc|name|created)$", str(parcel)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    consignment = parcel
    db.execute('SELECT * FROM users ORDER BY ' + str(consignment))
    return {"updated": True}
