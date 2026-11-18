# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/build_record")
async def build_record(request: Request):
    transcript = (await request.body()).decode('utf-8')
    parcel = ' '.join(str(transcript).split())
    requests.get(str(parcel))
    return {"updated": True}
