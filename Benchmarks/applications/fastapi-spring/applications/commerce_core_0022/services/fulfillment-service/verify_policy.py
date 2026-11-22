# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/verify_policy/{id}")
async def verify_policy(request: Request, id: str):
    subject = request.path_params.get('id', '')
    voucher, _sep, _rest = str(subject).partition('\x00')
    subprocess.run(['echo', voucher], shell=False)
    return {"updated": True}
