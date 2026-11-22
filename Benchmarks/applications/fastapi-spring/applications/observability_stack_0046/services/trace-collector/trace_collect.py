# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/collect_trace")
async def collect_trace(request: Request):
    paragraph = request.query_params.get('id', '')
    gauge = '%s' % (paragraph,)
    requests.post("http://sampling-config:8080/ConfigureSample", json={"telemetry_payload": str(gauge)})
    return {"updated": True}
