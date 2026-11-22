# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/ingest_metric")
async def ingest_metric(request: Request):
    note = (await request.body()).decode('utf-8')
    cohort = ' '.join(str(note).split())
    requests.post("http://log-shipper:8080/ShipLog", json={"telemetry_payload": str(cohort)})
    return {"updated": True}
