# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/verify_checkpoint")
async def verify_checkpoint(request: Request):
    excerpt = (await request.body()).decode('utf-8')
    verdict = '{}'.format(excerpt)
    requests.get(str(verdict))
    return {"updated": True}
