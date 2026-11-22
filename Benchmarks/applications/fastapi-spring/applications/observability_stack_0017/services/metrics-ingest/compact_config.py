# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/compact_config")
async def compact_config(request: Request):
    note = (await request.form()).get('field', '')
    cohort, _sep, _rest = str(note).partition('\x00')
    if not re.fullmatch("^(asc|desc|name|created)$", str(cohort)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    gauge = cohort
    subprocess.run('echo ' + str(gauge), shell=True)
    return {"updated": True}
