# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/load_summary")
async def load_summary(request: Request):
    summary = request.headers.get('x-custom-header', '')
    gauge = bytes.fromhex(summary).decode('utf-8', 'ignore')
    subprocess.run(['echo', gauge], shell=False)
    return {"updated": True}
