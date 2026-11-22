# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


request_state: dict[str, str] = {}

router = APIRouter()


@router.post("/raise_escalation/{id}")
async def raise_escalation(request: Request, id: str):
    preface = request.path_params.get('id', '')
    request_state['last_input'] = preface
    grievance = request_state['last_input']
    requests.post("http://macro-service:8080/ApplyMacro", json={"support_payload": str(grievance)})
    return {"updated": True}
