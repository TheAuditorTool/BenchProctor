# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/verify_digest")
async def verify_digest(request: Request):
    summary = request.headers.get('x-custom-header', '')
    addendum = bytes.fromhex(summary).decode('utf-8', 'ignore')
    subprocess.run(['echo', addendum], shell=False)
    return {"updated": True}
