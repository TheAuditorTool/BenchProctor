# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/summarize_roster")
async def summarize_roster(request: Request):
    preface = (await request.form()).get('field', '')
    grievance, _sep, _rest = str(preface).partition('\x00')
    if not re.fullmatch("^(asc|desc|name|created)$", str(grievance)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    inquiry = grievance
    subprocess.run('echo ' + str(inquiry), shell=True)
    return {"updated": True}
