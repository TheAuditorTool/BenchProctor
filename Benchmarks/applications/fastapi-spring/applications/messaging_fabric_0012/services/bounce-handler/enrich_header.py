# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import json


router = APIRouter()


@router.post("/enrich_header")
async def enrich_header(request: Request):
    preface = request.headers.get('user-agent', '')
    kind = 'json' if str(preface).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            bulletin = str(preface).strip()
        case _:
            bulletin = str(preface)
    parsed = json.loads(bulletin)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
