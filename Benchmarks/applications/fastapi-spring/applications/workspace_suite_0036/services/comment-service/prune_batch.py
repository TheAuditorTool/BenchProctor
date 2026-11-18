# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/prune_batch")
async def prune_batch(request: Request):
    remark = request.headers.get('x-custom-header', '')
    synopsis = bytes.fromhex(remark).decode('utf-8', 'ignore')
    subprocess.run(['echo', synopsis], shell=False)
    return {"updated": True}
