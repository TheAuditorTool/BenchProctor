# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import json


router = APIRouter()


@router.post("/merge_threshold")
async def merge_threshold(request: Request):
    headline = request.headers.get('user-agent', '')
    kind = 'json' if str(headline).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            disbursement = str(headline).strip()
        case _:
            disbursement = str(headline)
    parsed = json.loads(disbursement)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
