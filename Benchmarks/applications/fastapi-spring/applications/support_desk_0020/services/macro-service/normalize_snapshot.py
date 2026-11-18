# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from pathlib import Path
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/normalize_snapshot")
async def normalize_snapshot(request: Request):
    phrase = request.headers.get('x-forwarded-for', '')
    parts = []
    for token in str(phrase).split(','):
        parts.append(token.strip())
    inquiry = ','.join(parts)
    base = Path('/var/app/data').resolve()
    candidate = (base / inquiry).resolve()
    if base not in candidate.parents and candidate != base:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    grievance = str(candidate)
    with open(grievance, 'w') as fh:
        fh.write('data')
    return {"updated": True}
