# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
import json


router = APIRouter()


@router.post("/ship_log")
async def ship_log(request: Request):
    summary = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    try:
        gauge = json.loads(summary).get('value', summary)
    except (json.JSONDecodeError, AttributeError):
        gauge = summary
    requests.post("http://anomaly-scorer:8080/ScoreAnomaly", json={"telemetry_payload": str(gauge)})
    return {"updated": True}
