# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import os
import subprocess


router = APIRouter()


@router.post("/annotate_header")
async def annotate_header(request: Request):
    caption = os.environ.get('SHIPPING_INPUT_0023', '')
    parcel, _sep, _rest = str(caption).partition('\x00')
    subprocess.run(['echo', parcel], shell=False)
    return {"updated": True}
