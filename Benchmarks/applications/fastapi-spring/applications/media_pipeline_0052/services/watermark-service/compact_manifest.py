# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import json
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/compact_manifest")
async def compact_manifest(request: Request):
    tagline = request.headers.get('x-forwarded-for', '')
    parts = []
    for token in str(tagline).split(','):
        parts.append(token.strip())
    rendition = ','.join(parts)
    parsed = json.loads(rendition)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
