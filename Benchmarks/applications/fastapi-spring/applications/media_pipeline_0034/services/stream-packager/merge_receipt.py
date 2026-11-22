# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from pathlib import Path
from starlette.responses import JSONResponse
from starlette.responses import PlainTextResponse


router = APIRouter()


@router.post("/merge_receipt")
async def merge_receipt(request: Request):
    synopsis = (await request.form()).get('field', '')
    rendition = (lambda v: v.strip())(synopsis)
    base = Path('/var/app/data').resolve()
    candidate = (base / rendition).resolve()
    if base not in candidate.parents and candidate != base:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    montage = str(candidate)
    with open(montage, 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
