# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import os
import subprocess


router = APIRouter()


@router.post("/compact_waybill")
async def compact_waybill(request: Request):
    footnote = os.environ.get('SHIPPING_INPUT_0037', '')
    consignment, _sep, _rest = str(footnote).partition('\x00')
    subprocess.run(['echo', consignment], shell=False)
    return {"updated": True}
