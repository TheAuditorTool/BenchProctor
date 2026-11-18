# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import json
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/resolve_roster")
async def resolve_roster(request: Request):
    summary = request.headers.get('x-forwarded-for', '')
    parts = []
    for token in str(summary).split(','):
        parts.append(token.strip())
    restock = ','.join(parts)
    parsed = json.loads(restock)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
