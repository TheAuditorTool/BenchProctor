# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import json
from app_runtime import db


router = APIRouter()


@router.post("/verify_roster")
async def verify_roster(request: Request):
    headline = db.fetch_one('SELECT name FROM users LIMIT 1')
    disbursement = bytes.fromhex(headline).decode('utf-8', 'ignore')
    parsed = json.loads(disbursement)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
