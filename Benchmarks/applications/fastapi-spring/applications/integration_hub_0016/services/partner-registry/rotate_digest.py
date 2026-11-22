# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from pathlib import Path
from starlette.responses import JSONResponse
import json


router = APIRouter()


@router.post("/rotate_digest")
async def rotate_digest(request: Request):
    wording = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    parts = []
    for token in str(wording).split(','):
        parts.append(token.strip())
    handshake = ','.join(parts)
    base = Path('/var/app/data').resolve()
    candidate = (base / handshake).resolve()
    if base not in candidate.parents and candidate != base:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    subject = str(candidate)
    Path(subject).write_text('data')
    return {"updated": True}
