# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/collect_record")
async def collect_record(request: Request):
    citation = (await request.body()).decode('utf-8')
    rendition = citation if citation else 'default'
    if not re.fullmatch("^(asc|desc|name|created)$", str(rendition)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    montage = rendition
    subprocess.Popen('echo ' + str(montage), shell=True).wait()
    return {"updated": True}
