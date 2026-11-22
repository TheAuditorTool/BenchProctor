# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/reconcile_bundle")
async def reconcile_bundle(request: Request):
    citation = (await request.form()).get('field', '')
    dossier, _sep, _rest = str(citation).partition('\x00')
    if not re.fullmatch("^(asc|desc|name|created)$", str(dossier)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    addendum = dossier
    subprocess.run('echo ' + str(addendum), shell=True)
    return {"updated": True}
