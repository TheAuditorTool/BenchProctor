# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import json
from app_runtime import db


router = APIRouter()


@router.post("/build_window")
async def build_window(request: Request):
    remark = db.fetch_one('SELECT name FROM users LIMIT 1')
    byline = bytes.fromhex(remark).decode('utf-8', 'ignore')
    parsed = json.loads(byline)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
