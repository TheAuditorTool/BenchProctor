# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/validate_summary")
async def validate_summary(request: Request):
    caption = (await request.form()).get('field', '')
    remittance, _sep, _rest = str(caption).partition('\x00')
    if not re.fullmatch("^(asc|desc|name|created)$", str(remittance)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    dunning = remittance
    subprocess.run('echo ' + str(dunning), shell=True)
    return {"updated": True}
