# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import json
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/fetch_taxonomy")
async def fetch_taxonomy(request: Request):
    synopsis = request.headers.get('x-forwarded-for', '')
    parts = []
    for token in str(synopsis).split(','):
        parts.append(token.strip())
    byline = ','.join(parts)
    parsed = json.loads(byline)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
