# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


class RequestContext:
    def __init__(self, payload, source='http'):
        self.payload = payload
        self.source = source

router = APIRouter()


@router.post("/register_service")
async def register_service(request: Request):
    notice = (await request.body()).decode('utf-8')
    ctx = RequestContext(notice, source='form')
    persona = ctx.payload
    requests.post("http://config-service:8080/RolloutConfig", json={"platform_payload": str(persona)})
    return {"updated": True}
