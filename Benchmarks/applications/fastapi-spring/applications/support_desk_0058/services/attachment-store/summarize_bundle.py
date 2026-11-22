# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from pathlib import Path
from starlette.responses import JSONResponse
import json


router = APIRouter()


@router.post("/summarize_bundle")
async def summarize_bundle(request: Request):
    snippet = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    parts = []
    for token in str(snippet).split(','):
        parts.append(token.strip())
    inquiry = ','.join(parts)
    base = Path('/var/app/data').resolve()
    candidate = (base / inquiry).resolve()
    if base not in candidate.parents and candidate != base:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    grievance = str(candidate)
    Path(grievance).write_text('data')
    return {"updated": True}
