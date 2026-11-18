# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import base64
import os
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/resolve_release")
async def resolve_release(request: Request):
    footnote = request.headers.get('authorization', '')
    wording = base64.b64decode(footnote).decode('utf-8', 'ignore')
    if not re.fullmatch("^(asc|desc|name|created)$", str(wording)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    note = wording
    os.system('echo ' + str(note))
    return {"updated": True}
