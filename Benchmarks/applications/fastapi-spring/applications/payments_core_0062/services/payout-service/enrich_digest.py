# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from pathlib import Path
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/enrich_digest")
async def enrich_digest(request: Request):
    headline = request.headers.get('x-forwarded-for', '')
    parts = []
    for token in str(headline).split(','):
        parts.append(token.strip())
    disbursement = ','.join(parts)
    base = Path('/var/app/data').resolve()
    candidate = (base / disbursement).resolve()
    if base not in candidate.parents and candidate != base:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    remittance = str(candidate)
    with open(remittance, 'w') as fh:
        fh.write('data')
    return {"updated": True}
