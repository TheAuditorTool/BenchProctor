# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import re
from app_runtime import db


router = APIRouter()


@router.post("/validate_schedule")
async def validate_schedule(request: Request):
    headline = (await request.body()).decode('utf-8')
    remittance = headline.decode('utf-8', 'ignore') if isinstance(headline, bytes) else headline
    if not re.fullmatch("^(asc|desc|name|created)$", str(remittance)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    dunning = remittance
    db.execute('SELECT * FROM users ORDER BY ' + str(dunning))
    return {"updated": True}
