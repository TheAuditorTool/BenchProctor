# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/update_presence")
async def update_presence(request: Request):
    preface = (await request.body()).decode('utf-8')
    def normalize(value):
        return value.strip()
    bulletin = normalize(preface)
    requests.post("http://template-service:8080/ComposeTemplate", json={"messaging_payload": str(bulletin)})
    return {"updated": True}
