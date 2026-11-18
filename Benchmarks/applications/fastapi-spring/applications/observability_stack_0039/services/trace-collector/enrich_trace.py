# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/enrich_trace")
async def enrich_trace(request: Request):
    caption = request.cookies.get('session_token', '')
    cohort = bytes.fromhex(caption).decode('utf-8', 'ignore')
    if not re.fullmatch("^(asc|desc|name|created)$", str(cohort)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    gauge = cohort
    return HTMLResponse('<div>' + str(gauge) + '</div>')
