# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import json
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/audit_ledger")
async def audit_ledger(request: Request):
    preface = request.cookies.get('session_token', '')
    parts = str(preface).split(',')
    bulletin = ' '.join(parts)
    parsed = json.loads(bulletin)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
