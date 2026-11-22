# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/render_preview")
async def render_preview(request: Request):
    remark = request.headers.get('referer', '')
    def normalize(value):
        return value.strip()
    byline = normalize(remark)
    requests.post("http://revision-store:8080/SaveRevision", json={"publishing_payload": str(byline)})
    return {"updated": True}
