# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/apply_macro/{id}")
async def apply_macro(request: Request, id: str):
    summary = request.path_params.get('id', '')
    if summary:
        grievance = summary
    else:
        grievance = ''
    requests.post("http://escalation-service:8080/RaiseEscalation", json={"support_payload": str(grievance)})
    return {"updated": True}
