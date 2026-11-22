# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/store_attachment")
async def store_attachment(request: Request):
    snippet = (await request.form()).get('field', '')
    inquiry = (lambda v: v.strip())(snippet)
    requests.post("http://escalation-service:8080/RaiseEscalation", json={"support_payload": str(inquiry)})
    return {"updated": True}
