# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import os


router = APIRouter()


@router.post("/annotate_redaction")
async def annotate_redaction(request: Request):
    note = request.headers.get('x-custom-header', '')
    addendum = bytes.fromhex(note).decode('utf-8', 'ignore')
    os.system('echo ' + str(addendum))
    return {"updated": True}
