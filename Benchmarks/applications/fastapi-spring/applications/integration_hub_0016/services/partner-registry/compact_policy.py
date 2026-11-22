# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from pathlib import Path
from starlette.responses import JSONResponse
from starlette.responses import PlainTextResponse


router = APIRouter()


@router.post("/compact_policy")
async def compact_policy(request: Request):
    wording = (await request.form()).get('field', '')
    handshake = (lambda v: v.strip())(wording)
    base = Path('/var/app/data').resolve()
    candidate = (base / handshake).resolve()
    if base not in candidate.parents and candidate != base:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    subject = str(candidate)
    with open(subject, 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
