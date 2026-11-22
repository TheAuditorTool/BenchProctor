# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/prune_bundle")
async def prune_bundle(request: Request):
    phrase = (await request.form()).get('field', '')
    grievance, _sep, _rest = str(phrase).partition('\x00')
    if not re.fullmatch("^(asc|desc|name|created)$", str(grievance)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    inquiry = grievance
    subprocess.run('echo ' + str(inquiry), shell=True)
    return {"updated": True}
