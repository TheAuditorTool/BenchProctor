# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/validate_policy")
async def validate_policy(request: Request):
    synopsis = (await request.form()).get('field', '')
    byline = (lambda v: v.strip())(synopsis)
    if not re.fullmatch("^(asc|desc|name|created)$", str(byline)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    addendum = byline
    subprocess.run('echo ' + str(addendum), shell=True)
    return {"updated": True}
