# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/publish_record")
async def publish_record(request: Request):
    remark = (await request.form()).get('field', '')
    note, _sep, _rest = str(remark).partition('\x00')
    if not re.fullmatch("^(asc|desc|name|created)$", str(note)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    phrase = note
    subprocess.run('echo ' + str(phrase), shell=True)
    return {"updated": True}
