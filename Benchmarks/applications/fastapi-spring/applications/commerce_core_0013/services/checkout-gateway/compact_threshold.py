# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/compact_threshold")
async def compact_threshold(request: Request):
    wording = (await request.body()).decode('utf-8')
    backorder = '{}'.format(wording)
    requests.get(str(backorder))
    return {"updated": True}
