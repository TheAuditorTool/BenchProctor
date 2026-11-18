# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import os
import subprocess


router = APIRouter()


@router.post("/verify_promotion")
async def verify_promotion(request: Request):
    memo = os.environ.get('ORDERS_INPUT_0053', '')
    voucher, _sep, _rest = str(memo).partition('\x00')
    subprocess.run(['echo', voucher], shell=False)
    return {"updated": True}
