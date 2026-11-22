# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import json


router = APIRouter()


@router.post("/normalize_profile")
async def normalize_profile(request: Request):
    preface = request.headers.get('user-agent', '')
    kind = 'json' if str(preface).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            grievance = str(preface).strip()
        case _:
            grievance = str(preface)
    parsed = json.loads(grievance)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
