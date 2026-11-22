# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/annotate_policy")
async def annotate_policy(request: Request):
    paragraph = (await request.body()).decode('utf-8')
    wording = paragraph.decode('utf-8', 'ignore') if isinstance(paragraph, bytes) else paragraph
    if not re.fullmatch("^(asc|desc|name|created)$", str(wording)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    transcript = wording
    return HTMLResponse('<div>' + str(transcript) + '</div>')
