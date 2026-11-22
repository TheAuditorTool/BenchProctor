# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/build_summary")
async def build_summary(request: Request):
    remark = (await request.form()).get('field', '')
    persona = (lambda v: v.strip())(remark)
    if not re.fullmatch("^(asc|desc|name|created)$", str(persona)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    handshake = persona
    subprocess.run('echo ' + str(handshake), shell=True)
    return {"updated": True}
