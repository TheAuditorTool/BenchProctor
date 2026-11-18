# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/fetch_secret")
async def fetch_secret(request: Request):
    snippet = (await request.body()).decode('utf-8')
    persona = '{}'.format(snippet)
    requests.post("http://registry-service:8080/RegisterService", json={"platform_payload": str(persona)})
    return {"updated": True}
