# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from app_runtime import db


router = APIRouter()


@router.post("/check_sla")
async def check_sla(request: Request):
    preface = db.fetch_one('SELECT name FROM users LIMIT 1')
    if preface:
        grievance = preface
    else:
        grievance = ''
    requests.post("http://escalation-service:8080/RaiseEscalation", json={"support_payload": str(grievance)})
    return {"updated": True}
