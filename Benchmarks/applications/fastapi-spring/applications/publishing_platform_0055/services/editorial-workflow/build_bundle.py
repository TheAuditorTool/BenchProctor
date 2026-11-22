# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import json


router = APIRouter()


@router.post("/build_bundle")
async def build_bundle(request: Request):
    synopsis = request.headers.get('user-agent', '')
    kind = 'json' if str(synopsis).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            byline = str(synopsis).strip()
        case _:
            byline = str(synopsis)
    parsed = json.loads(byline)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
