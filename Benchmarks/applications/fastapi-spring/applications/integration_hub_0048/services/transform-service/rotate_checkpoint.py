# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import json
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/rotate_checkpoint")
async def rotate_checkpoint(request: Request):
    citation = request.cookies.get('session_token', '')
    parts = str(citation).split(',')
    handshake = ' '.join(parts)
    parsed = json.loads(handshake)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
