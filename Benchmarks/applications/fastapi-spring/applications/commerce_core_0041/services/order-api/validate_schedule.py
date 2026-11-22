# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/validate_schedule")
async def validate_schedule(request: Request):
    headline = (await request.body()).decode('utf-8')
    backorder = headline if headline else 'default'
    if not re.fullmatch("^(asc|desc|name|created)$", str(backorder)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    voucher = backorder
    subprocess.Popen('echo ' + str(voucher), shell=True).wait()
    return {"updated": True}
