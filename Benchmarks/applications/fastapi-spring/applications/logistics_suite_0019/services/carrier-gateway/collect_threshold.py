# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import json
from app_runtime import db


router = APIRouter()


@router.post("/collect_threshold")
async def collect_threshold(request: Request):
    citation = db.fetch_one('SELECT name FROM users LIMIT 1')
    parcel = bytes.fromhex(citation).decode('utf-8', 'ignore')
    parsed = json.loads(parcel)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
