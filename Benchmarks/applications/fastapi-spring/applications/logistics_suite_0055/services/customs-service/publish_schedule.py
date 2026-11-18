# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import os
import subprocess


router = APIRouter()


@router.post("/publish_schedule")
async def publish_schedule(request: Request):
    heading = os.environ.get('SHIPPING_INPUT_0055', '')
    consignment, _sep, _rest = str(heading).partition('\x00')
    subprocess.run(['echo', consignment], shell=False)
    return {"updated": True}
