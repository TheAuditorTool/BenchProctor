# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/rotate_delivery")
async def rotate_delivery(request: Request):
    paragraph = request.headers.get('x-custom-header', '')
    bulletin = bytes.fromhex(paragraph).decode('utf-8', 'ignore')
    subprocess.run(['echo', bulletin], shell=False)
    return {"updated": True}
