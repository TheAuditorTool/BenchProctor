# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/reconcile_batch")
async def reconcile_batch(request: Request):
    preface = (await request.body()).decode('utf-8')
    bulletin = preface if preface else 'default'
    if not re.fullmatch("^(asc|desc|name|created)$", str(bulletin)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    citation = bulletin
    subprocess.Popen('echo ' + str(citation), shell=True).wait()
    return {"updated": True}
