# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/archive_schedule")
async def archive_schedule(request: Request):
    phrase = (await request.body()).decode('utf-8')
    dossier = phrase.decode('utf-8', 'ignore') if isinstance(phrase, bytes) else phrase
    if not re.fullmatch("^(asc|desc|name|created)$", str(dossier)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    addendum = dossier
    return HTMLResponse('<div>' + str(addendum) + '</div>')
