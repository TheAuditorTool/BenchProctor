# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/publish_config")
async def publish_config(request: Request):
    headline = (await request.form()).get('field', '')
    backorder, _sep, _rest = str(headline).partition('\x00')
    if not re.fullmatch("^(asc|desc|name|created)$", str(backorder)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    voucher = backorder
    subprocess.run('echo ' + str(voucher), shell=True)
    return {"updated": True}
