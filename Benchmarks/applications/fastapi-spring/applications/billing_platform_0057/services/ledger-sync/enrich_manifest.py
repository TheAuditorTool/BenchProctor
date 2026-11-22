# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/enrich_manifest")
async def enrich_manifest(request: Request):
    caption = (await request.body()).decode('utf-8')
    remittance = caption if caption else 'default'
    if not re.fullmatch("^(asc|desc|name|created)$", str(remittance)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    dunning = remittance
    subprocess.Popen('echo ' + str(dunning), shell=True).wait()
    return {"updated": True}
