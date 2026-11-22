# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/archive_index")
async def archive_index(request: Request):
    excerpt = (await request.form()).get('field', '')
    cohort = (lambda v: v.strip())(excerpt)
    if not re.fullmatch("^(asc|desc|name|created)$", str(cohort)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    gauge = cohort
    subprocess.run('echo ' + str(gauge), shell=True)
    return {"updated": True}
