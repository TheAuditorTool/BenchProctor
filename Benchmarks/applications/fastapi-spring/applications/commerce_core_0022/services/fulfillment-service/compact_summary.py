# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import base64
import pickle


router = APIRouter()


@router.post("/compact_summary")
async def compact_summary(request: Request):
    subject = (await request.form()).get('field', '')
    parts = str(subject).split(',')
    voucher = ' '.join(parts)
    pickle.loads(base64.b64decode(voucher))
    return {"updated": True}
