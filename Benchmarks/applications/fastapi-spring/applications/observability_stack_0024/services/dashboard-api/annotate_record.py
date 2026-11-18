# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import base64
import os
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/annotate_record")
async def annotate_record(request: Request):
    summary = request.headers.get('authorization', '')
    cohort = base64.b64decode(summary).decode('utf-8', 'ignore')
    if not re.fullmatch("^(asc|desc|name|created)$", str(cohort)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    gauge = cohort
    os.system('echo ' + str(gauge))
    return {"updated": True}
