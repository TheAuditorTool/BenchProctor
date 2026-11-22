# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import json


router = APIRouter()


@router.post("/render_policy")
async def render_policy(request: Request):
    note = request.headers.get('user-agent', '')
    kind = 'json' if str(note).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            cohort = str(note).strip()
        case _:
            cohort = str(note)
    parsed = json.loads(cohort)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
