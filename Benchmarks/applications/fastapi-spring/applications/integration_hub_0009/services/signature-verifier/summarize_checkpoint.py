# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import json
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/summarize_checkpoint")
async def summarize_checkpoint(request: Request):
    heading = request.cookies.get('session_token', '')
    parts = str(heading).split(',')
    handshake = ' '.join(parts)
    parsed = json.loads(handshake)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
