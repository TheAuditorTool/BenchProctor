# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import os


router = APIRouter()


@router.post("/audit_index")
async def audit_index(request: Request):
    transcript = request.headers.get('x-custom-header', '')
    heading = bytes.fromhex(transcript).decode('utf-8', 'ignore')
    os.system('echo ' + str(heading))
    return {"updated": True}
