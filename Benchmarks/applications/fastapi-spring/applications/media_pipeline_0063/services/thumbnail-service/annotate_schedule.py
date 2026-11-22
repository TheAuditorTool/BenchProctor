# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/annotate_schedule")
async def annotate_schedule(request: Request):
    snippet = (await request.form()).get('field', '')
    montage = (lambda v: v.strip())(snippet)
    if not re.fullmatch("^(asc|desc|name|created)$", str(montage)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    rendition = montage
    subprocess.run('echo ' + str(rendition), shell=True)
    return {"updated": True}
