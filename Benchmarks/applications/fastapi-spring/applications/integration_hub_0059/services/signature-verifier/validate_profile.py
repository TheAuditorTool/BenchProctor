# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/validate_profile")
async def validate_profile(request: Request):
    synopsis = (await request.body()).decode('utf-8')
    handshake = ' '.join(str(synopsis).split())
    requests.get(str(handshake))
    return {"updated": True}
