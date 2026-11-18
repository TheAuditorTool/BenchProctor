# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/ship_log/{id}")
async def ship_log(request: Request, id: str):
    caption = request.path_params.get('id', '')
    kind = 'json' if str(caption).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            gauge = str(caption).strip()
        case _:
            gauge = str(caption)
    requests.post("http://metrics-ingest:8080/IngestMetric", json={"telemetry_payload": str(gauge)})
    return {"updated": True}
