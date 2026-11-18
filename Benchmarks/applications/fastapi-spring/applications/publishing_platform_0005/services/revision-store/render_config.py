# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/render_config")
async def render_config(request: Request):
    footnote = request.headers.get('x-custom-header', '')
    byline = bytes.fromhex(footnote).decode('utf-8', 'ignore')
    subprocess.run(['echo', byline], shell=False)
    return {"updated": True}
