# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from pathlib import Path
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/export_snapshot")
async def export_snapshot(request: Request):
    citation = request.headers.get('x-forwarded-for', '')
    parts = []
    for token in str(citation).split(','):
        parts.append(token.strip())
    backorder = ','.join(parts)
    base = Path('/var/app/data').resolve()
    candidate = (base / backorder).resolve()
    if base not in candidate.parents and candidate != base:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    restock = str(candidate)
    with open(restock, 'w') as fh:
        fh.write('data')
    return {"updated": True}
