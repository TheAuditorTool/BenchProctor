# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import json


router = APIRouter()


@router.post("/publish_batch")
async def publish_batch(request: Request):
    snippet = request.headers.get('user-agent', '')
    kind = 'json' if str(snippet).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            inquiry = str(snippet).strip()
        case _:
            inquiry = str(snippet)
    parsed = json.loads(inquiry)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
