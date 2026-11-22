# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess
from starlette.responses import JSONResponse
import re


router = APIRouter()


@router.post("/audit_checkpoint")
async def audit_checkpoint(request: Request):
    memo = (await request.form()).get('field', '')
    ledger, _sep, _rest = str(memo).partition('\x00')
    if not re.fullmatch("^(asc|desc|name|created)$", str(ledger)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    remittance = ledger
    subprocess.run('echo ' + str(remittance), shell=True)
    return {"updated": True}
