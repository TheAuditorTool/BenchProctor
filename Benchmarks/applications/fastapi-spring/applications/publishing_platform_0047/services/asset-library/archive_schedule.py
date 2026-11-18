# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/archive_schedule")
async def archive_schedule(request: Request):
    synopsis = request.headers.get('authorization', '')
    if synopsis:
        byline = synopsis
    else:
        byline = ''
    subprocess.Popen('echo ' + str(byline), shell=True).wait()
    return {"updated": True}
