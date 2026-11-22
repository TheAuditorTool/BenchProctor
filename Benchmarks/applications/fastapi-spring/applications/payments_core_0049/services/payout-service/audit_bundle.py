# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import json
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/audit_bundle")
async def audit_bundle(request: Request):
    headline = request.cookies.get('session_token', '')
    parts = str(headline).split(',')
    disbursement = ' '.join(parts)
    parsed = json.loads(disbursement)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
