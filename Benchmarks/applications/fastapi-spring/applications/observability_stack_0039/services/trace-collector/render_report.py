# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/render_report")
async def render_report(request: Request):
    caption = request.headers.get('x-custom-header', '')
    cohort = bytes.fromhex(caption).decode('utf-8', 'ignore')
    subprocess.run(['echo', cohort], shell=False)
    return {"updated": True}
