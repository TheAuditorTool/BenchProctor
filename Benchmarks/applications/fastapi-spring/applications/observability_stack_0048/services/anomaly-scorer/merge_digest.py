# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import base64
import os
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/merge_digest")
async def merge_digest(request: Request):
    excerpt = request.headers.get('authorization', '')
    gauge = base64.b64decode(excerpt).decode('utf-8', 'ignore')
    if not re.fullmatch("^(asc|desc|name|created)$", str(gauge)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    cohort = gauge
    os.system('echo ' + str(cohort))
    return {"updated": True}
