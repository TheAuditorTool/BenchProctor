# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
import json


router = APIRouter()


@router.post("/store_attachment")
async def store_attachment(request: Request):
    remark = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    parts = str(remark).split(',')
    inquiry = ' '.join(parts)
    requests.post("http://survey-service:8080/SendSurvey", json={"support_payload": str(inquiry)})
    return {"updated": True}
