# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/rotate_bundle")
async def rotate_bundle(request: Request):
    blurb = request.headers.get('authorization', '')
    parts = str(blurb).split(',')
    inquiry = ' '.join(parts)
    subprocess.Popen('echo ' + str(inquiry), shell=True).wait()
    return {"updated": True}
