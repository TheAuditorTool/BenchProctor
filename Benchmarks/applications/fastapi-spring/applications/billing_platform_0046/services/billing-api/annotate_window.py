# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from pathlib import Path
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/annotate_window")
async def annotate_window(request: Request):
    remark = request.headers.get('x-forwarded-for', '')
    parts = []
    for token in str(remark).split(','):
        parts.append(token.strip())
    remittance = ','.join(parts)
    base = Path('/var/app/data').resolve()
    candidate = (base / remittance).resolve()
    if base not in candidate.parents and candidate != base:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    arrears = str(candidate)
    with open(arrears, 'w') as fh:
        fh.write('data')
    return {"updated": True}
