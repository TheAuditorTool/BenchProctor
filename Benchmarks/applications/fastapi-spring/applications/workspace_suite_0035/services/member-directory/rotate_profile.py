# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from pathlib import Path
from starlette.responses import JSONResponse
from starlette.responses import PlainTextResponse


router = APIRouter()


@router.post("/rotate_profile")
async def rotate_profile(request: Request):
    paragraph = (await request.form()).get('field', '')
    wording = (lambda v: v.strip())(paragraph)
    base = Path('/var/app/data').resolve()
    candidate = (base / wording).resolve()
    if base not in candidate.parents and candidate != base:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    transcript = str(candidate)
    with open(transcript, 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
