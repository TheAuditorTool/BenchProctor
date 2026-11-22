# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/post_ledger_entry")
async def post_ledger_entry(request: Request):
    caption = (await request.form()).get('field', '')
    parts = str(caption).split(',')
    remittance = ' '.join(parts)
    requests.post("http://payment-gateway:8080/CapturePayment", json={"billing_payload": str(remittance)})
    return {"updated": True}
