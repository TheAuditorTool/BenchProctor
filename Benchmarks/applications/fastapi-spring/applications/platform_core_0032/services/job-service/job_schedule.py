# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/schedule_job")
async def schedule_job(request: Request):
    remark = (await request.form()).get('field', '')
    persona, _sep, _rest = str(remark).partition('\x00')
    requests.post("http://quota-service:8080/EnforceQuota", json={"platform_payload": str(persona)})
    return {"updated": True}
