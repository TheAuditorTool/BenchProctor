# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/archive_escalation")
async def archive_escalation(request: Request):
    phrase = (await request.body()).decode('utf-8')
    grievance = phrase.decode('utf-8', 'ignore') if isinstance(phrase, bytes) else phrase
    if not re.fullmatch("^(asc|desc|name|created)$", str(grievance)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    inquiry = grievance
    return HTMLResponse('<div>' + str(inquiry) + '</div>')
