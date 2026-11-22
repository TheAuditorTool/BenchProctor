# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import json
from app_runtime import db


router = APIRouter()


@router.post("/render_window")
async def render_window(request: Request):
    wording = db.fetch_one('SELECT name FROM users LIMIT 1')
    handshake = bytes.fromhex(wording).decode('utf-8', 'ignore')
    parsed = json.loads(handshake)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
