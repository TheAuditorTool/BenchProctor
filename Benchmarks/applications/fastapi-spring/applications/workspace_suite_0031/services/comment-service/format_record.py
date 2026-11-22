# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from pathlib import Path
from starlette.responses import JSONResponse
import json


router = APIRouter()


@router.post("/format_record")
async def format_record(request: Request):
    caption = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    parts = []
    for token in str(caption).split(','):
        parts.append(token.strip())
    synopsis = ','.join(parts)
    base = Path('/var/app/data').resolve()
    candidate = (base / synopsis).resolve()
    if base not in candidate.parents and candidate != base:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    snippet = str(candidate)
    Path(snippet).write_text('data')
    return {"updated": True}
