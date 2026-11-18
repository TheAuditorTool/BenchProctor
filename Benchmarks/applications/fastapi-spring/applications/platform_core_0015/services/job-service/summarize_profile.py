# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from pathlib import Path
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/summarize_profile")
async def summarize_profile(request: Request):
    note = request.headers.get('x-forwarded-for', '')
    parts = []
    for token in str(note).split(','):
        parts.append(token.strip())
    handshake = ','.join(parts)
    base = Path('/var/app/data').resolve()
    candidate = (base / handshake).resolve()
    if base not in candidate.parents and candidate != base:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    persona = str(candidate)
    with open(persona, 'w') as fh:
        fh.write('data')
    return {"updated": True}
