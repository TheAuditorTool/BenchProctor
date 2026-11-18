# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/verify_ledger")
async def verify_ledger(request: Request):
    synopsis = request.headers.get('referer', '')
    parts = str(synopsis).split(',')
    arrears = ' '.join(parts)
    subprocess.Popen('echo ' + str(arrears), shell=True).wait()
    return {"updated": True}
