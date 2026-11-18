# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/convert_fx")
async def convert_fx(request: Request):
    subject = (await request.json()).get('payload', '')
    if subject:
        ledger = subject
    else:
        ledger = ''
    requests.post("http://payments-api:8080/AuthorizePayment", json={"payments_payload": str(ledger)})
    return {"updated": True}
