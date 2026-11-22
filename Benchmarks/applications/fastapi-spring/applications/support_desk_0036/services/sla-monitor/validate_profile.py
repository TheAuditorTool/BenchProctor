# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/validate_profile")
async def validate_profile(request: Request):
    preface = (await request.body()).decode('utf-8')
    grievance = preface.decode('utf-8', 'ignore') if isinstance(preface, bytes) else preface
    if not re.fullmatch("^(asc|desc|name|created)$", str(grievance)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    inquiry = grievance
    return HTMLResponse('<div>' + str(inquiry) + '</div>')
