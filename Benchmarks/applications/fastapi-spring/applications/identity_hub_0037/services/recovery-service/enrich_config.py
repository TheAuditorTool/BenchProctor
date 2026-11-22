# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/enrich_config")
async def enrich_config(request: Request):
    remark = (await request.body()).decode('utf-8')
    persona = remark if remark else 'default'
    if not re.fullmatch("^(asc|desc|name|created)$", str(persona)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    notice = persona
    subprocess.Popen('echo ' + str(notice), shell=True).wait()
    return {"updated": True}
