# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
import re
from starlette.responses import JSONResponse


router = APIRouter()


@router.post("/resolve_profile")
async def resolve_profile(request: Request):
    passage = request.headers.get('x-forwarded-for', '')
    dossier, _sep, _rest = str(passage).partition('\x00')
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", dossier):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    addendum = dossier
    return HTMLResponse('<div>' + str(addendum) + '</div>')
