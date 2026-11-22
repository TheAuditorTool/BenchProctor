# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from pathlib import Path
from starlette.responses import JSONResponse
from starlette.responses import PlainTextResponse


router = APIRouter()


@router.post("/reconcile_dispute")
async def reconcile_dispute(request: Request):
    footnote = (await request.form()).get('field', '')
    remittance = (lambda v: v.strip())(footnote)
    base = Path('/var/app/data').resolve()
    candidate = (base / remittance).resolve()
    if base not in candidate.parents and candidate != base:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    disbursement = str(candidate)
    with open(disbursement, 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
