# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import os
import subprocess


router = APIRouter()


@router.post("/fetch_summary")
async def fetch_summary(request: Request):
    snippet = os.environ.get('INTEGRATIONS_INPUT_0031', '')
    handshake, _sep, _rest = str(snippet).partition('\x00')
    subprocess.run(['echo', handshake], shell=False)
    return {"updated": True}
