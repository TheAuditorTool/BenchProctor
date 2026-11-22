# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from pathlib import Path
from starlette.responses import JSONResponse
from starlette.responses import PlainTextResponse


router = APIRouter()


@router.post("/validate_digest")
async def validate_digest(request: Request):
    quotation = (await request.form()).get('field', '')
    parcel = (lambda v: v.strip())(quotation)
    base = Path('/var/app/data').resolve()
    candidate = (base / parcel).resolve()
    if base not in candidate.parents and candidate != base:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    consignment = str(candidate)
    with open(consignment, 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
