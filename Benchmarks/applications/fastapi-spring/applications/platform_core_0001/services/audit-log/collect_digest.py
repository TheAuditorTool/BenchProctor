# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import os
import subprocess


router = APIRouter()


@router.post("/collect_digest")
async def collect_digest(request: Request):
    tagline = os.environ.get('PLATFORM_INPUT_0001', '')
    persona, _sep, _rest = str(tagline).partition('\x00')
    subprocess.run(['echo', persona], shell=False)
    return {"updated": True}
