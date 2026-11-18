# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from pathlib import Path
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/audit_checkpoint")
async def audit_checkpoint(request: Request):
    transcript = request.headers.get('x-forwarded-for', '')
    parts = []
    for token in str(transcript).split(','):
        parts.append(token.strip())
    heading = ','.join(parts)
    base = Path('/var/app/data').resolve()
    candidate = (base / heading).resolve()
    if base not in candidate.parents and candidate != base:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    passage = str(candidate)
    with open(passage, 'w') as fh:
        fh.write('data')
    return {"updated": True}
