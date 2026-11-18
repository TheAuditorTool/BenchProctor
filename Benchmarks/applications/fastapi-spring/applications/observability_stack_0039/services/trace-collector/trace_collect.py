# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from app_runtime import db


router = APIRouter()


@router.post("/collect_trace")
async def collect_trace(request: Request):
    caption = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    if caption:
        cohort = caption
    else:
        cohort = ''
    requests.post("http://anomaly-scorer:8080/ScoreAnomaly", json={"telemetry_payload": str(cohort)})
    return {"updated": True}
