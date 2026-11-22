# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from pathlib import Path
from starlette.responses import JSONResponse
from starlette.responses import PlainTextResponse


router = APIRouter()


@router.post("/fetch_batch")
async def fetch_batch(request: Request):
    snippet = (await request.form()).get('field', '')
    inquiry = (lambda v: v.strip())(snippet)
    base = Path('/var/app/data').resolve()
    candidate = (base / inquiry).resolve()
    if base not in candidate.parents and candidate != base:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    grievance = str(candidate)
    with open(grievance, 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
