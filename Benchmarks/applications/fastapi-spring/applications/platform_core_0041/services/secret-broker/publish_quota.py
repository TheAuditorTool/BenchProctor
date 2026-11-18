# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import yaml
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/publish_quota")
async def publish_quota(request: Request):
    passage = request.headers.get('host', '')
    pending = list(str(passage).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    persona = ','.join(collected)
    parsed = yaml.safe_load(persona)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
