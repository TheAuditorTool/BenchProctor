# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import json
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/audit_ledger")
async def audit_ledger(request: Request):
    citation = request.cookies.get('session_token', '')
    parts = str(citation).split(',')
    consignment = ' '.join(parts)
    parsed = json.loads(consignment)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
