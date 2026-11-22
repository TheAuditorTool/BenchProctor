# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/publish_report")
async def publish_report(request: Request):
    note = (await request.body()).decode('utf-8')
    byline = note if note else 'default'
    if not re.fullmatch("^(asc|desc|name|created)$", str(byline)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    addendum = byline
    subprocess.Popen('echo ' + str(addendum), shell=True).wait()
    return {"updated": True}
