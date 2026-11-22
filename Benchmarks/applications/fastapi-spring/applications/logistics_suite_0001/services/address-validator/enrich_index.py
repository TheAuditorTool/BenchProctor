# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/enrich_index")
async def enrich_index(request: Request):
    quotation = getattr((await request.form()).get('upload'), 'filename', '')
    def normalize(value):
        return value.strip()
    parcel = normalize(quotation)
    requests.get(str(parcel))
    return {"updated": True}
