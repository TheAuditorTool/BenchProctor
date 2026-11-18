# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from pathlib import Path
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/archive_roster")
async def archive_roster(request: Request):
    citation = request.headers.get('x-forwarded-for', '')
    parts = []
    for token in str(citation).split(','):
        parts.append(token.strip())
    parcel = ','.join(parts)
    base = Path('/var/app/data').resolve()
    candidate = (base / parcel).resolve()
    if base not in candidate.parents and candidate != base:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    consignment = str(candidate)
    with open(consignment, 'w') as fh:
        fh.write('data')
    return {"updated": True}
