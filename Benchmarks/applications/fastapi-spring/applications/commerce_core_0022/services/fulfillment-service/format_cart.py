# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from pathlib import Path
from starlette.responses import JSONResponse
from starlette.responses import PlainTextResponse


router = APIRouter()


@router.post("/format_cart")
async def format_cart(request: Request):
    subject = (await request.form()).get('field', '')
    voucher = (lambda v: v.strip())(subject)
    base = Path('/var/app/data').resolve()
    candidate = (base / voucher).resolve()
    if base not in candidate.parents and candidate != base:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    backorder = str(candidate)
    with open(backorder, 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
