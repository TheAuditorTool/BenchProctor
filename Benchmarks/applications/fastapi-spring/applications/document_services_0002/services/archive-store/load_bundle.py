# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/load_bundle")
async def load_bundle(request: Request):
    wording = (await request.body()).decode('utf-8')
    addendum = wording if wording else 'default'
    if not re.fullmatch("^(asc|desc|name|created)$", str(addendum)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    dossier = addendum
    subprocess.Popen('echo ' + str(dossier), shell=True).wait()
    return {"updated": True}
