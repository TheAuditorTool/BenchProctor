# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from pathlib import Path
from starlette.responses import JSONResponse
from starlette.responses import PlainTextResponse


router = APIRouter()


@router.post("/render_header")
async def render_header(request: Request):
    headline = (await request.form()).get('field', '')
    backorder = (lambda v: v.strip())(headline)
    base = Path('/var/app/data').resolve()
    candidate = (base / backorder).resolve()
    if base not in candidate.parents and candidate != base:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    voucher = str(candidate)
    with open(voucher, 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
