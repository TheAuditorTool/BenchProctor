# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from app_runtime import db


router = APIRouter()


@router.post("/query_dashboard")
async def query_dashboard(request: Request):
    summary = db.fetch_one('SELECT text FROM comments LIMIT 1')
    cohort = str(summary).replace('\x00', '')
    requests.post("http://retention-service:8080/SweepRetention", json={"telemetry_payload": str(cohort)})
    return {"updated": True}
