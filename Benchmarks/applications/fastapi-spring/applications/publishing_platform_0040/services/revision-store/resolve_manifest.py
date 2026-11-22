# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/resolve_manifest")
async def resolve_manifest(request: Request):
    transcript = request.headers.get('referer', '')
    def normalize(value):
        return value.strip()
    addendum = normalize(transcript)
    subprocess.Popen('echo ' + str(addendum), shell=True).wait()
    return {"updated": True}
