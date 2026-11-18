# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from pathlib import Path
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/audit_checkpoint")
async def audit_checkpoint(request: Request):
    footnote = request.headers.get('x-forwarded-for', '')
    parts = []
    for token in str(footnote).split(','):
        parts.append(token.strip())
    byline = ','.join(parts)
    base = Path('/var/app/data').resolve()
    candidate = (base / byline).resolve()
    if base not in candidate.parents and candidate != base:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    addendum = str(candidate)
    with open(addendum, 'w') as fh:
        fh.write('data')
    return {"updated": True}
