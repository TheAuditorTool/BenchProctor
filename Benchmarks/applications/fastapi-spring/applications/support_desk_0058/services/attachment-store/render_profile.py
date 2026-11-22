# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/render_profile")
async def render_profile(request: Request):
    snippet = (await request.form()).get('field', '')
    inquiry, _sep, _rest = str(snippet).partition('\x00')
    if not re.fullmatch("^(asc|desc|name|created)$", str(inquiry)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    grievance = inquiry
    subprocess.run('echo ' + str(grievance), shell=True)
    return {"updated": True}
