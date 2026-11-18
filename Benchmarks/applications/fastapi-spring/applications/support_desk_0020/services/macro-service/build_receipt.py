# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import json
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/build_receipt")
async def build_receipt(request: Request):
    phrase = request.headers.get('x-forwarded-for', '')
    parts = []
    for token in str(phrase).split(','):
        parts.append(token.strip())
    inquiry = ','.join(parts)
    parsed = json.loads(inquiry)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
