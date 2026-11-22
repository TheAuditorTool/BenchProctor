# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import json
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/annotate_window")
async def annotate_window(request: Request):
    subtitle = request.cookies.get('session_token', '')
    parts = str(subtitle).split(',')
    persona = ' '.join(parts)
    parsed = json.loads(persona)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
