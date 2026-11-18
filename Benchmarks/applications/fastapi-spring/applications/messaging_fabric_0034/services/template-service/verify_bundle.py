# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import json
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/verify_bundle")
async def verify_bundle(request: Request):
    footnote = request.headers.get('x-forwarded-for', '')
    parts = []
    for token in str(footnote).split(','):
        parts.append(token.strip())
    bulletin = ','.join(parts)
    parsed = json.loads(bulletin)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
