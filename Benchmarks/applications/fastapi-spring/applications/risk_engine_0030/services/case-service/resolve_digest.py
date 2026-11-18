# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import base64
import os
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/resolve_digest")
async def resolve_digest(request: Request):
    summary = request.headers.get('authorization', '')
    grievance = base64.b64decode(summary).decode('utf-8', 'ignore')
    if not re.fullmatch("^(asc|desc|name|created)$", str(grievance)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    verdict = grievance
    os.system('echo ' + str(verdict))
    return {"updated": True}
