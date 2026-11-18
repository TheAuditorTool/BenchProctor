# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import yaml
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/publish_schedule")
async def publish_schedule(request: Request):
    summary = request.headers.get('host', '')
    pending = list(str(summary).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    bulletin = ','.join(collected)
    parsed = yaml.safe_load(bulletin)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
