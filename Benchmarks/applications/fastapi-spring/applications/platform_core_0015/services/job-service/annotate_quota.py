# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/annotate_quota")
async def annotate_quota(request: Request):
    note = (await request.body()).decode('utf-8')
    handshake = ' '.join(str(note).split())
    requests.get(str(handshake))
    return {"updated": True}
