# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/check_sla")
async def check_sla(request: Request):
    phrase = request.headers.get('referer', '')
    grievance = phrase if phrase else 'default'
    requests.post("http://ticket-router:8080/RouteTicket", json={"support_payload": str(grievance)})
    return {"updated": True}
