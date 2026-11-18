# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/publish_message")
async def publish_message(request: Request):
    summary = request.headers.get('user-agent', '')
    requests.post("http://bounce-handler:8080/RecordBounce", json={"messaging_payload": str(summary)})
    return {"updated": True}
