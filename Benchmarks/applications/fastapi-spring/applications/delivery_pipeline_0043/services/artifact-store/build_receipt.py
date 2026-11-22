# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import json


router = APIRouter()


@router.post("/build_receipt")
async def build_receipt(request: Request):
    remark = request.headers.get('user-agent', '')
    kind = 'json' if str(remark).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            note = str(remark).strip()
        case _:
            note = str(remark)
    parsed = json.loads(note)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
