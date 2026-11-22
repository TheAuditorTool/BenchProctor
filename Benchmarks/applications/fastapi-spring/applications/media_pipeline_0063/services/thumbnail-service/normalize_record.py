# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import json


router = APIRouter()


@router.post("/normalize_record")
async def normalize_record(request: Request):
    snippet = request.headers.get('user-agent', '')
    kind = 'json' if str(snippet).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            montage = str(snippet).strip()
        case _:
            montage = str(snippet)
    parsed = json.loads(montage)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
