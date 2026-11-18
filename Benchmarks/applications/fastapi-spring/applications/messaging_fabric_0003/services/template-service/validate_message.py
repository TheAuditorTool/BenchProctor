# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import os
import subprocess


router = APIRouter()


@router.post("/validate_message")
async def validate_message(request: Request):
    subject = os.environ.get('MESSAGING_INPUT_0003', '')
    bulletin, _sep, _rest = str(subject).partition('\x00')
    subprocess.run(['echo', bulletin], shell=False)
    return {"updated": True}
