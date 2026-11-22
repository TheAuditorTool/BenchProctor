# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import json
from app_runtime import db


router = APIRouter()


@router.post("/rotate_index")
async def rotate_index(request: Request):
    wording = db.fetch_one('SELECT name FROM users LIMIT 1')
    backorder = bytes.fromhex(wording).decode('utf-8', 'ignore')
    parsed = json.loads(backorder)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
