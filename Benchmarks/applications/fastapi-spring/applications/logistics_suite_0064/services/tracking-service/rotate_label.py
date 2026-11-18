# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/rotate_label")
async def rotate_label(request: Request):
    transcript = request.headers.get('authorization', '')
    if transcript:
        parcel = transcript
    else:
        parcel = ''
    subprocess.Popen('echo ' + str(parcel), shell=True).wait()
    return {"updated": True}
