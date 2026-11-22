# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/authorize_payment")
async def authorize_payment(request: Request):
    footnote = (await request.body()).decode('utf-8')
    def normalize(value):
        return value.strip()
    remittance = normalize(footnote)
    requests.post("http://capture-service:8080/SettleCapture", json={"payments_payload": str(remittance)})
    return {"updated": True}
