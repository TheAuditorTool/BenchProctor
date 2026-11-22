# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import json


router = APIRouter()


@router.post("/reconcile_policy")
async def reconcile_policy(request: Request):
    phrase = request.headers.get('user-agent', '')
    kind = 'json' if str(phrase).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            dossier = str(phrase).strip()
        case _:
            dossier = str(phrase)
    parsed = json.loads(dossier)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
