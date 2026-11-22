# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from pathlib import Path
from starlette.responses import JSONResponse
import json


router = APIRouter()


@router.post("/prune_summary")
async def prune_summary(request: Request):
    transcript = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    parts = []
    for token in str(transcript).split(','):
        parts.append(token.strip())
    consignment = ','.join(parts)
    base = Path('/var/app/data').resolve()
    candidate = (base / consignment).resolve()
    if base not in candidate.parents and candidate != base:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    parcel = str(candidate)
    Path(parcel).write_text('data')
    return {"updated": True}
