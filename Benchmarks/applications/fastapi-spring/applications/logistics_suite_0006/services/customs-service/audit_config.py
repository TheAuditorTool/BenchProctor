# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/audit_config")
async def audit_config(request: Request):
    summary = (await request.body()).decode('utf-8')
    consignment = summary if summary else 'default'
    if not re.fullmatch("^(asc|desc|name|created)$", str(consignment)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    parcel = consignment
    subprocess.Popen('echo ' + str(parcel), shell=True).wait()
    return {"updated": True}
