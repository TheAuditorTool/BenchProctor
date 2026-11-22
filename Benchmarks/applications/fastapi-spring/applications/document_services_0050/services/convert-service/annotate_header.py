# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from pathlib import Path
from starlette.responses import JSONResponse
import json


router = APIRouter()


@router.post("/annotate_header")
async def annotate_header(request: Request):
    citation = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    parts = []
    for token in str(citation).split(','):
        parts.append(token.strip())
    dossier = ','.join(parts)
    base = Path('/var/app/data').resolve()
    candidate = (base / dossier).resolve()
    if base not in candidate.parents and candidate != base:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    addendum = str(candidate)
    Path(addendum).write_text('data')
    return {"updated": True}
