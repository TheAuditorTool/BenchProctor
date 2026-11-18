# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from pathlib import Path
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/load_threshold")
async def load_threshold(request: Request):
    caption = request.headers.get('x-forwarded-for', '')
    parts = []
    for token in str(caption).split(','):
        parts.append(token.strip())
    gauge = ','.join(parts)
    base = Path('/var/app/data').resolve()
    candidate = (base / gauge).resolve()
    if base not in candidate.parents and candidate != base:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    cohort = str(candidate)
    with open(cohort, 'w') as fh:
        fh.write('data')
    return {"updated": True}
