# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import json
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/publish_config")
async def publish_config(request: Request):
    snippet = request.cookies.get('session_token', '')
    parts = str(snippet).split(',')
    montage = ' '.join(parts)
    parsed = json.loads(montage)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
