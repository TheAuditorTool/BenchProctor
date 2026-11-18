# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import base64
import os
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/enrich_bundle")
async def enrich_bundle(request: Request):
    note = request.headers.get('authorization', '')
    inquiry = base64.b64decode(note).decode('utf-8', 'ignore')
    if not re.fullmatch("^(asc|desc|name|created)$", str(inquiry)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    grievance = inquiry
    os.system('echo ' + str(grievance))
    return {"updated": True}
