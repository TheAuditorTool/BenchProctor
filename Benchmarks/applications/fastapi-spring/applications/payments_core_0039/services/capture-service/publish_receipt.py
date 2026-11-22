# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import re
from app_runtime import db


router = APIRouter()


@router.post("/publish_receipt")
async def publish_receipt(request: Request):
    memo = (await request.body()).decode('utf-8')
    ledger = memo.decode('utf-8', 'ignore') if isinstance(memo, bytes) else memo
    if not re.fullmatch("^(asc|desc|name|created)$", str(ledger)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    remittance = ledger
    db.execute('SELECT * FROM users ORDER BY ' + str(remittance))
    return {"updated": True}
