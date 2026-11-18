# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import os
import subprocess


router = APIRouter()


@router.post("/audit_roster")
async def audit_roster(request: Request):
    transcript = os.environ.get('WORKSPACE_INPUT_0002', '')
    heading, _sep, _rest = str(transcript).partition('\x00')
    subprocess.run(['echo', heading], shell=False)
    return {"updated": True}
