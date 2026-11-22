# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/configure_sample")
async def configure_sample(request: Request):
    remark = (await request.body()).decode('utf-8')
    gauge = remark.decode('utf-8', 'ignore') if isinstance(remark, bytes) else remark
    requests.post("http://retention-service:8080/SweepRetention", json={"telemetry_payload": str(gauge)})
    return {"updated": True}
