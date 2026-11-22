# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import json


router = APIRouter()


@router.post("/audit_membership")
async def audit_membership(request: Request):
    paragraph = request.headers.get('user-agent', '')
    kind = 'json' if str(paragraph).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            wording = str(paragraph).strip()
        case _:
            wording = str(paragraph)
    parsed = json.loads(wording)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
