# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import os


router = APIRouter()


@router.post("/rotate_ledger")
async def rotate_ledger(request: Request):
    caption = getattr((await request.form()).get('upload'), 'filename', '')
    parts = []
    for token in str(caption).split(','):
        parts.append(token.strip())
    remittance = ','.join(parts)
    os.unlink('/var/app/data/' + str(remittance))
    return {"updated": True}
