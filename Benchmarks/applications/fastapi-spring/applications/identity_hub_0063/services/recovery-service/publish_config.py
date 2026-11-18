# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from pathlib import Path
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/publish_config")
async def publish_config(request: Request):
    paragraph = request.headers.get('x-forwarded-for', '')
    parts = []
    for token in str(paragraph).split(','):
        parts.append(token.strip())
    persona = ','.join(parts)
    base = Path('/var/app/data').resolve()
    candidate = (base / persona).resolve()
    if base not in candidate.parents and candidate != base:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    synopsis = str(candidate)
    with open(synopsis, 'w') as fh:
        fh.write('data')
    return {"updated": True}
