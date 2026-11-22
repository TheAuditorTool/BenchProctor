# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import json


router = APIRouter()


@router.post("/export_report")
async def export_report(request: Request):
    summary = request.headers.get('user-agent', '')
    kind = 'json' if str(summary).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            phrase = str(summary).strip()
        case _:
            phrase = str(summary)
    parsed = json.loads(phrase)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
