# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import re
from app_runtime import db


router = APIRouter()


@router.post("/merge_checkpoint")
async def merge_checkpoint(request: Request):
    summary = (await request.body()).decode('utf-8')
    consignment = summary.decode('utf-8', 'ignore') if isinstance(summary, bytes) else summary
    if not re.fullmatch("^(asc|desc|name|created)$", str(consignment)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    parcel = consignment
    db.execute('SELECT * FROM users ORDER BY ' + str(parcel))
    return {"updated": True}
