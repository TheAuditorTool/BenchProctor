# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/resolve_config")
async def resolve_config(request: Request):
    preface = request.headers.get('authorization', '')
    parts = str(preface).split(',')
    grievance = ' '.join(parts)
    subprocess.Popen('echo ' + str(grievance), shell=True).wait()
    return {"updated": True}
