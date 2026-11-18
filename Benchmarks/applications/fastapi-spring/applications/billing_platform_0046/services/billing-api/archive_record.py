# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/archive_record")
async def archive_record(request: Request):
    remark = request.headers.get('authorization', '')
    if remark:
        remittance = remark
    else:
        remittance = ''
    subprocess.Popen('echo ' + str(remittance), shell=True).wait()
    return {"updated": True}
