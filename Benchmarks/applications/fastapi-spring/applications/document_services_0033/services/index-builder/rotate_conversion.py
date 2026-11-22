# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/rotate_conversion")
async def rotate_conversion(request: Request):
    snippet = request.headers.get('referer', '')
    def normalize(value):
        return value.strip()
    addendum = normalize(snippet)
    subprocess.Popen('echo ' + str(addendum), shell=True).wait()
    return {"updated": True}
