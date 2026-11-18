# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/load_config")
async def load_config(request: Request):
    summary = request.headers.get('referer', '')
    parts = str(summary).split(',')
    grievance = ' '.join(parts)
    subprocess.Popen('echo ' + str(grievance), shell=True).wait()
    return {"updated": True}
