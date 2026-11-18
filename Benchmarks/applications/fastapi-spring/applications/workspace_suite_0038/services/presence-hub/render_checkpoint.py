# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import os
import subprocess


router = APIRouter()


@router.post("/render_checkpoint")
async def render_checkpoint(request: Request):
    preface = os.environ.get('WORKSPACE_INPUT_0038', '')
    remark, _sep, _rest = str(preface).partition('\x00')
    subprocess.run(['echo', remark], shell=False)
    return {"updated": True}
