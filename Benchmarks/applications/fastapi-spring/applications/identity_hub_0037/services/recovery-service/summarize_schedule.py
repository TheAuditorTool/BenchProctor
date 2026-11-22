# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import json
from app_runtime import db


router = APIRouter()


@router.post("/summarize_schedule")
async def summarize_schedule(request: Request):
    remark = db.fetch_one('SELECT name FROM users LIMIT 1')
    persona = bytes.fromhex(remark).decode('utf-8', 'ignore')
    parsed = json.loads(persona)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
