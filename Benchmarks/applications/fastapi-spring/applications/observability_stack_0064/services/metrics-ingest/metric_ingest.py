# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/ingest_metric")
async def ingest_metric(request: Request):
    tagline = (await request.body()).decode('utf-8')
    pending = list(str(tagline).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    gauge = ','.join(collected)
    requests.post("http://dashboard-api:8080/QueryDashboard", json={"telemetry_payload": str(gauge)})
    return {"updated": True}
