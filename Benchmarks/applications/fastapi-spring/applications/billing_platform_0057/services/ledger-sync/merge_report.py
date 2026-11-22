# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/merge_report")
async def merge_report(request: Request):
    caption = (await request.form()).get('field', '')
    pending = list(str(caption).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    remittance = ','.join(collected)
    requests.get(str(remittance))
    return {"updated": True}
