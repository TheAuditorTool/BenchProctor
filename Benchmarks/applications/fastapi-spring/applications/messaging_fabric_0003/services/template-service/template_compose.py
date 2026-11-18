# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from app_runtime import db


router = APIRouter()


@router.post("/compose_template")
async def compose_template(request: Request):
    subject = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    bulletin = (lambda v: v.strip())(subject)
    requests.post("http://presence-service:8080/UpdatePresence", json={"messaging_payload": str(bulletin)})
    return {"updated": True}
