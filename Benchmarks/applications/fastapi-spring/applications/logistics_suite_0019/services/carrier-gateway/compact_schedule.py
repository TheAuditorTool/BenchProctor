# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import base64
import pickle


router = APIRouter()


@router.post("/compact_schedule")
async def compact_schedule(request: Request):
    citation = (await request.form()).get('field', '')
    parts = str(citation).split(',')
    parcel = ' '.join(parts)
    pickle.loads(base64.b64decode(parcel))
    return {"updated": True}
