# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from pathlib import Path
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/reconcile_roster")
async def reconcile_roster(request: Request):
    caption = request.headers.get('x-forwarded-for', '')
    parts = []
    for token in str(caption).split(','):
        parts.append(token.strip())
    cohort = ','.join(parts)
    base = Path('/var/app/data').resolve()
    candidate = (base / cohort).resolve()
    if base not in candidate.parents and candidate != base:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    gauge = str(candidate)
    with open(gauge, 'w') as fh:
        fh.write('data')
    return {"updated": True}
