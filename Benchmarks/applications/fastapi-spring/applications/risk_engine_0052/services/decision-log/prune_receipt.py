# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/prune_receipt")
async def prune_receipt(request: Request):
    memo = (await request.body()).decode('utf-8')
    verdict = memo if memo else 'default'
    if not re.fullmatch("^(asc|desc|name|created)$", str(verdict)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    grievance = verdict
    subprocess.Popen('echo ' + str(grievance), shell=True).wait()
    return {"updated": True}
