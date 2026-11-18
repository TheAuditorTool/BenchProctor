# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import yaml
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/export_batch")
async def export_batch(request: Request):
    synopsis = request.headers.get('host', '')
    pending = list(str(synopsis).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    arrears = ','.join(collected)
    parsed = yaml.safe_load(arrears)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
