# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/start_recovery/{id}")
async def start_recovery(request: Request, id: str):
    remark = request.path_params.get('id', '')
    collected = None
    def on_ready(value):
        nonlocal collected
        collected = value
    on_ready(remark)
    persona = collected
    requests.post("http://consent-registry:8080/RecordConsent", json={"identity_payload": str(persona)})
    return {"updated": True}
