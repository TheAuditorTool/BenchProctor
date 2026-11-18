# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import json
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/publish_report")
async def publish_report(request: Request):
    footnote = request.headers.get('x-forwarded-for', '')
    parts = []
    for token in str(footnote).split(','):
        parts.append(token.strip())
    handshake = ','.join(parts)
    parsed = json.loads(handshake)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
