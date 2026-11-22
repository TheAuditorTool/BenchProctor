# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import json
from app_runtime import db


router = APIRouter()


@router.post("/merge_index")
async def merge_index(request: Request):
    memo = db.fetch_one('SELECT name FROM users LIMIT 1')
    ledger = bytes.fromhex(memo).decode('utf-8', 'ignore')
    parsed = json.loads(ledger)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
