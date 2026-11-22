# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/audit_report")
async def audit_report(request: Request):
    footnote = request.headers.get('authorization', '')
    parts = str(footnote).split(',')
    remittance = ' '.join(parts)
    subprocess.Popen('echo ' + str(remittance), shell=True).wait()
    return {"updated": True}
