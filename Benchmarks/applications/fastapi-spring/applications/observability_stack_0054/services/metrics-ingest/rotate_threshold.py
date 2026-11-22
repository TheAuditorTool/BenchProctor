# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import json


router = APIRouter()


@router.post("/rotate_threshold")
async def rotate_threshold(request: Request):
    excerpt = request.headers.get('user-agent', '')
    kind = 'json' if str(excerpt).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            cohort = str(excerpt).strip()
        case _:
            cohort = str(excerpt)
    parsed = json.loads(cohort)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
