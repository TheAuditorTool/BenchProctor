# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import json
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/collect_profile")
async def collect_profile(request: Request):
    summary = request.headers.get('x-forwarded-for', '')
    parts = []
    for token in str(summary).split(','):
        parts.append(token.strip())
    grievance = ','.join(parts)
    parsed = json.loads(grievance)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
