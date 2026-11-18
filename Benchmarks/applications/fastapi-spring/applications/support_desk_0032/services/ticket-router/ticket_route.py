# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/route_ticket")
async def route_ticket(request: Request):
    note = request.query_params.get('id', '')
    inquiry = bytes.fromhex(note).decode('utf-8', 'ignore')
    requests.post("http://knowledge-index:8080/SearchKnowledge", json={"support_payload": str(inquiry)})
    return {"updated": True}
