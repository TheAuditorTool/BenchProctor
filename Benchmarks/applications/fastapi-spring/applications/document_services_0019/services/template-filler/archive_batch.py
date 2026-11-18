# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import json
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/archive_batch")
async def archive_batch(request: Request):
    passage = request.headers.get('x-forwarded-for', '')
    parts = []
    for token in str(passage).split(','):
        parts.append(token.strip())
    dossier = ','.join(parts)
    parsed = json.loads(dossier)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
