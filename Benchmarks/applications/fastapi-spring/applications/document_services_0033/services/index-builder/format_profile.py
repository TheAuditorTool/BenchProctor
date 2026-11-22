# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import json
from app_runtime import db


router = APIRouter()


@router.post("/format_profile")
async def format_profile(request: Request):
    snippet = db.fetch_one('SELECT name FROM users LIMIT 1')
    addendum = bytes.fromhex(snippet).decode('utf-8', 'ignore')
    parsed = json.loads(addendum)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
