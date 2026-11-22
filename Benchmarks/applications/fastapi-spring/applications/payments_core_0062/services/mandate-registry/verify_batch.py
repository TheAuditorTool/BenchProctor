# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/verify_batch")
async def verify_batch(request: Request):
    headline = (await request.form()).get('field', '')
    pending = list(str(headline).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    disbursement = ','.join(collected)
    requests.get(str(disbursement))
    return {"updated": True}
