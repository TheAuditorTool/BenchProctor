# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/ingest_metric")
async def ingest_metric(request: Request):
    excerpt = request.headers.get('x-forwarded-for', '')
    cohort = excerpt if excerpt else 'default'
    requests.post("http://sampling-config:8080/ConfigureSample", json={"telemetry_payload": str(cohort)})
    return {"updated": True}
