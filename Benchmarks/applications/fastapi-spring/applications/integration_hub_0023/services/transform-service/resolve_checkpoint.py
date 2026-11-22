# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/resolve_checkpoint")
async def resolve_checkpoint(request: Request):
    caption = (await request.form()).get('field', '')
    handshake = (lambda v: v.strip())(caption)
    if not re.fullmatch("^(asc|desc|name|created)$", str(handshake)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    subject = handshake
    subprocess.run('echo ' + str(subject), shell=True)
    return {"updated": True}
