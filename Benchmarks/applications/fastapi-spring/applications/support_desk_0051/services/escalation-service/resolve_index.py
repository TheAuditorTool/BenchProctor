# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from pathlib import Path
from starlette.responses import JSONResponse
from starlette.responses import PlainTextResponse


router = APIRouter()


@router.post("/resolve_index")
async def resolve_index(request: Request):
    preface = (await request.form()).get('field', '')
    grievance = (lambda v: v.strip())(preface)
    base = Path('/var/app/data').resolve()
    candidate = (base / grievance).resolve()
    if base not in candidate.parents and candidate != base:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    inquiry = str(candidate)
    with open(inquiry, 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
