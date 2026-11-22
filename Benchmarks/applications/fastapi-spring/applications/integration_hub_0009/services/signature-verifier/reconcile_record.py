# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/reconcile_record")
async def reconcile_record(request: Request):
    heading = (await request.body()).decode('utf-8')
    handshake = heading if heading else 'default'
    if not re.fullmatch("^(asc|desc|name|created)$", str(handshake)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    remark = handshake
    subprocess.Popen('echo ' + str(remark), shell=True).wait()
    return {"updated": True}
