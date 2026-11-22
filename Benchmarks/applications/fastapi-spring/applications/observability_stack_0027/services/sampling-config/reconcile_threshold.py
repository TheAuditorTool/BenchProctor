# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from pathlib import Path
from starlette.responses import JSONResponse
import json


router = APIRouter()


@router.post("/reconcile_threshold")
async def reconcile_threshold(request: Request):
    remark = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    parts = []
    for token in str(remark).split(','):
        parts.append(token.strip())
    gauge = ','.join(parts)
    base = Path('/var/app/data').resolve()
    candidate = (base / gauge).resolve()
    if base not in candidate.parents and candidate != base:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    cohort = str(candidate)
    Path(cohort).write_text('data')
    return {"updated": True}
