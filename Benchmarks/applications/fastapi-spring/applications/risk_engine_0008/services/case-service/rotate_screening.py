# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
import re
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/rotate_screening")
async def rotate_screening(request: Request):
    synopsis = request.headers.get('x-forwarded-for', '')
    verdict, _sep, _rest = str(synopsis).partition('\x00')
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", verdict):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    grievance = verdict
    return HTMLResponse('<div>' + str(grievance) + '</div>')
