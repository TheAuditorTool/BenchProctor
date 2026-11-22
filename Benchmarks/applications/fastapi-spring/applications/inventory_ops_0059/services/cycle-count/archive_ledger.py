# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from pathlib import Path
from starlette.responses import JSONResponse
import json


router = APIRouter()


@router.post("/archive_ledger")
async def archive_ledger(request: Request):
    memo = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    parts = []
    for token in str(memo).split(','):
        parts.append(token.strip())
    backorder = ','.join(parts)
    base = Path('/var/app/data').resolve()
    candidate = (base / backorder).resolve()
    if base not in candidate.parents and candidate != base:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    restock = str(candidate)
    Path(restock).write_text('data')
    return {"updated": True}
