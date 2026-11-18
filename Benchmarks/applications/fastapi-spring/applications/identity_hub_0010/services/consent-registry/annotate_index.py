# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/annotate_index")
async def annotate_index(request: Request):
    phrase = request.headers.get('referer', '')
    parts = str(phrase).split(',')
    persona = ' '.join(parts)
    subprocess.Popen('echo ' + str(persona), shell=True).wait()
    return {"updated": True}
