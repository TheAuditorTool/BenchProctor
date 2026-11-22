# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/store_attachment")
async def store_attachment(request: Request):
    blurb = request.headers.get('user-agent', '')
    inquiry, _sep, _rest = str(blurb).partition('\x00')
    requests.post("http://knowledge-index:8080/SearchKnowledge", json={"support_payload": str(inquiry)})
    return {"updated": True}
