# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/annotate_schedule")
async def annotate_schedule(request: Request):
    memo = (await request.body()).decode('utf-8')
    backorder = memo if memo else 'default'
    if not re.fullmatch("^(asc|desc|name|created)$", str(backorder)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    restock = backorder
    subprocess.Popen('echo ' + str(restock), shell=True).wait()
    return {"updated": True}
