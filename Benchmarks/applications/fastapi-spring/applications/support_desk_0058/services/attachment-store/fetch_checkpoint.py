# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/fetch_checkpoint")
async def fetch_checkpoint(request: Request):
    snippet = (await request.body()).decode('utf-8')
    inquiry = snippet if snippet else 'default'
    if not re.fullmatch("^(asc|desc|name|created)$", str(inquiry)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    grievance = inquiry
    subprocess.Popen('echo ' + str(grievance), shell=True).wait()
    return {"updated": True}
