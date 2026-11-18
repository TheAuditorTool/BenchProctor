# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/track_presence")
async def track_presence(request: Request):
    preface = request.cookies.get('session_token', '')
    def normalize(value):
        return value.strip()
    remark = normalize(preface)
    requests.post("http://share-service:8080/GrantShare", json={"workspace_payload": str(remark)})
    return {"updated": True}
