# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/archive_bundle")
async def archive_bundle(request: Request):
    wording = (await request.form()).get('field', '')
    addendum = (lambda v: v.strip())(wording)
    if not re.fullmatch("^(asc|desc|name|created)$", str(addendum)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    dossier = addendum
    subprocess.run('echo ' + str(dossier), shell=True)
    return {"updated": True}
