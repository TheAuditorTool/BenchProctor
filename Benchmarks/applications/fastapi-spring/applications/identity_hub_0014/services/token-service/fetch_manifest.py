# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import json
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/fetch_manifest")
async def fetch_manifest(request: Request):
    snippet = request.headers.get('x-forwarded-for', '')
    parts = []
    for token in str(snippet).split(','):
        parts.append(token.strip())
    persona = ','.join(parts)
    parsed = json.loads(persona)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
