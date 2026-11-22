# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from app_runtime import db


router = APIRouter()


@router.post("/roll_digest")
async def roll_digest(request: Request):
    footnote = db.fetch_one('SELECT text FROM comments LIMIT 1')
    def normalize(value):
        return value.strip()
    bulletin = normalize(footnote)
    requests.post("http://presence-service:8080/UpdatePresence", json={"messaging_payload": str(bulletin)})
    return {"updated": True}
