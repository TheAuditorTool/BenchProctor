# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import yaml
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/merge_summary")
async def merge_summary(request: Request):
    summary = request.headers.get('host', '')
    pending = list(str(summary).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    grievance = ','.join(collected)
    parsed = yaml.safe_load(grievance)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
