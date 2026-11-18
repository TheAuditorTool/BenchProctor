# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from pathlib import Path
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/load_record")
async def load_record(request: Request):
    subject = request.headers.get('x-forwarded-for', '')
    parts = []
    for token in str(subject).split(','):
        parts.append(token.strip())
    bulletin = ','.join(parts)
    base = Path('/var/app/data').resolve()
    candidate = (base / bulletin).resolve()
    if base not in candidate.parents and candidate != base:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    passage = str(candidate)
    with open(passage, 'w') as fh:
        fh.write('data')
    return {"updated": True}
