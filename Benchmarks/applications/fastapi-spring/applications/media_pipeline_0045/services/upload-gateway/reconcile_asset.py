# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import yaml
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/reconcile_asset")
async def reconcile_asset(request: Request):
    notice = request.headers.get('host', '')
    pending = list(str(notice).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    rendition = ','.join(collected)
    parsed = yaml.safe_load(rendition)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
