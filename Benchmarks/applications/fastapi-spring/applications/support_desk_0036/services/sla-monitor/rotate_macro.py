# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import json
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/rotate_macro")
async def rotate_macro(request: Request):
    preface = request.cookies.get('session_token', '')
    parts = str(preface).split(',')
    grievance = ' '.join(parts)
    parsed = json.loads(grievance)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
