# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from pathlib import Path
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/prune_record")
async def prune_record(request: Request):
    tagline = request.headers.get('x-forwarded-for', '')
    parts = []
    for token in str(tagline).split(','):
        parts.append(token.strip())
    persona = ','.join(parts)
    base = Path('/var/app/data').resolve()
    candidate = (base / persona).resolve()
    if base not in candidate.parents and candidate != base:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    handshake = str(candidate)
    with open(handshake, 'w') as fh:
        fh.write('data')
    return {"updated": True}
