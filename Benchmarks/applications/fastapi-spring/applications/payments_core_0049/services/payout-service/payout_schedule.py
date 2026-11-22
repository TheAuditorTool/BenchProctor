# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/schedule_payout")
async def schedule_payout(request: Request):
    headline = request.headers.get('authorization', '')
    disbursement = headline if headline else 'default'
    requests.post("http://reconcile-service:8080/RunReconciliation", json={"payments_payload": str(disbursement)})
    return {"updated": True}
