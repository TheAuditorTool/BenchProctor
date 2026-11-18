# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/compact_batch")
async def compact_batch(request: Request):
    note = request.headers.get('x-custom-header', '')
    handshake = bytes.fromhex(note).decode('utf-8', 'ignore')
    subprocess.run(['echo', handshake], shell=False)
    return {"updated": True}
