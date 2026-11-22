# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from pathlib import Path
from starlette.responses import JSONResponse
from starlette.responses import PlainTextResponse


router = APIRouter()


@router.post("/collect_window")
async def collect_window(request: Request):
    heading = (await request.form()).get('field', '')
    addendum = (lambda v: v.strip())(heading)
    base = Path('/var/app/data').resolve()
    candidate = (base / addendum).resolve()
    if base not in candidate.parents and candidate != base:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    byline = str(candidate)
    with open(byline, 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
