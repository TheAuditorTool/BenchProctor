# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/export_alert")
async def export_alert(request: Request):
    tagline = (await request.body()).decode('utf-8')
    gauge = tagline if tagline else 'default'
    if not re.fullmatch("^(asc|desc|name|created)$", str(gauge)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    cohort = gauge
    subprocess.Popen('echo ' + str(cohort), shell=True).wait()
    return {"updated": True}
