# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/sweep_retention")
async def sweep_retention(request: Request):
    headline = request.headers.get('origin', '')
    pending = list(str(headline).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    cohort = ','.join(collected)
    requests.post("http://dashboard-api:8080/QueryDashboard", json={"telemetry_payload": str(cohort)})
    return {"updated": True}
