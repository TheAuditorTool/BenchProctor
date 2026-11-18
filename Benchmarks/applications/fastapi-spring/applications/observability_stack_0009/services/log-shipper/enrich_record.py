# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/enrich_record")
async def enrich_record(request: Request):
    summary = request.cookies.get('session_token', '')
    gauge = bytes.fromhex(summary).decode('utf-8', 'ignore')
    if not re.fullmatch("^(asc|desc|name|created)$", str(gauge)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    cohort = gauge
    return HTMLResponse('<div>' + str(cohort) + '</div>')
