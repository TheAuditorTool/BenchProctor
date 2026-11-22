# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/enrich_article")
async def enrich_article(request: Request):
    transcript = (await request.body()).decode('utf-8')
    addendum = transcript.decode('utf-8', 'ignore') if isinstance(transcript, bytes) else transcript
    if not re.fullmatch("^(asc|desc|name|created)$", str(addendum)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    byline = addendum
    return HTMLResponse('<div>' + str(byline) + '</div>')
