# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/verify_profile")
async def verify_profile(request: Request):
    transcript = request.headers.get('x-custom-header', '')
    backorder = bytes.fromhex(transcript).decode('utf-8', 'ignore')
    subprocess.run(['echo', backorder], shell=False)
    return {"updated": True}
