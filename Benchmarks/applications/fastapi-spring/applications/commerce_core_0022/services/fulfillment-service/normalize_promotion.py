# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/normalize_promotion")
async def normalize_promotion(request: Request):
    subject = request.headers.get('authorization', '')
    parts = str(subject).split(',')
    voucher = ' '.join(parts)
    subprocess.Popen('echo ' + str(voucher), shell=True).wait()
    return {"updated": True}
