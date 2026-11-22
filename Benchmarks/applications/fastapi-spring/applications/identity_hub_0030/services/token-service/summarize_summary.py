# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/summarize_summary")
async def summarize_summary(request: Request):
    tagline = request.headers.get('referer', '')
    def normalize(value):
        return value.strip()
    persona = normalize(tagline)
    subprocess.Popen('echo ' + str(persona), shell=True).wait()
    return {"updated": True}
