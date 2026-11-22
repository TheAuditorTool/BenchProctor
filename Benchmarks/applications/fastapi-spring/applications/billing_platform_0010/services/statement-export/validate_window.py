# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import json
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/validate_window")
async def validate_window(request: Request):
    headline = request.cookies.get('session_token', '')
    parts = str(headline).split(',')
    remittance = ' '.join(parts)
    parsed = json.loads(remittance)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
