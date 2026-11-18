# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import yaml
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/render_summary")
async def render_summary(request: Request):
    phrase = request.headers.get('host', '')
    pending = list(str(phrase).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    persona = ','.join(collected)
    parsed = yaml.safe_load(persona)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
