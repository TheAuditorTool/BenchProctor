# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/fetch_threshold")
async def fetch_threshold(request: Request):
    citation = (await request.body()).decode('utf-8')
    dossier = citation if citation else 'default'
    if not re.fullmatch("^(asc|desc|name|created)$", str(dossier)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    addendum = dossier
    subprocess.Popen('echo ' + str(addendum), shell=True).wait()
    return {"updated": True}
