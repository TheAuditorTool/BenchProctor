# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/submit_invoice")
async def submit_invoice(request: Request):
    remark = request.headers.get('x-forwarded-for', '')
    remittance, _sep, _rest = str(remark).partition('\x00')
    requests.post("http://settlement-service:8080/RunSettlement", json={"billing_payload": str(remittance)})
    return {"updated": True}
