# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import json
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/rotate_fulfillment")
async def rotate_fulfillment(request: Request):
    notice = request.cookies.get('session_token', '')
    parts = str(notice).split(',')
    backorder = ' '.join(parts)
    parsed = json.loads(backorder)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
