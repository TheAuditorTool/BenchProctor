# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/annotate_profile")
async def annotate_profile(request: Request):
    paragraph = request.headers.get('authorization', '')
    if paragraph:
        bulletin = paragraph
    else:
        bulletin = ''
    subprocess.Popen('echo ' + str(bulletin), shell=True).wait()
    return {"updated": True}
