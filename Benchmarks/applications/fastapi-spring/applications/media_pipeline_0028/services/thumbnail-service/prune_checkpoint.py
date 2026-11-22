# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/prune_checkpoint")
async def prune_checkpoint(request: Request):
    citation = (await request.form()).get('field', '')
    rendition, _sep, _rest = str(citation).partition('\x00')
    if not re.fullmatch("^(asc|desc|name|created)$", str(rendition)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    montage = rendition
    subprocess.run('echo ' + str(montage), shell=True)
    return {"updated": True}
