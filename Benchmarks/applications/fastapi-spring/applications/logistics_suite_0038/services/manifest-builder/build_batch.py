# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import re
from app_runtime import db


router = APIRouter()


@router.post("/build_batch")
async def build_batch(request: Request):
    wording = (await request.body()).decode('utf-8')
    consignment = wording.decode('utf-8', 'ignore') if isinstance(wording, bytes) else wording
    if not re.fullmatch("^(asc|desc|name|created)$", str(consignment)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    parcel = consignment
    db.execute('SELECT * FROM users ORDER BY ' + str(parcel))
    return {"updated": True}
