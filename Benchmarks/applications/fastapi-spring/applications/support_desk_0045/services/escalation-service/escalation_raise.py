# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


def make_reader(raw):
    def read():
        return raw.strip()
    return read

router = APIRouter()


@router.post("/raise_escalation")
async def raise_escalation(request: Request):
    remark = request.headers.get('referer', '')
    reader = make_reader(remark)
    inquiry = reader()
    requests.post("http://knowledge-index:8080/SearchKnowledge", json={"support_payload": str(inquiry)})
    return {"updated": True}
