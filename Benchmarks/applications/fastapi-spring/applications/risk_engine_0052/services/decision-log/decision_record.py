# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/record_decision")
async def record_decision(request: Request):
    memo = (await request.body()).decode('utf-8')
    verdict = '{}'.format(memo)
    requests.post("http://screening-service:8080/RunScreening", json={"risk_payload": str(verdict)})
    return {"updated": True}
