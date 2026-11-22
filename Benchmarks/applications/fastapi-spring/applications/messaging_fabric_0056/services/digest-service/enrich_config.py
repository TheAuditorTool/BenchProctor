# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import json


router = APIRouter()


@router.post("/enrich_config")
async def enrich_config(request: Request):
    footnote = request.headers.get('user-agent', '')
    kind = 'json' if str(footnote).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            bulletin = str(footnote).strip()
        case _:
            bulletin = str(footnote)
    parsed = json.loads(bulletin)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
