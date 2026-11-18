# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests


router = APIRouter()


@router.post("/roll_digest")
async def roll_digest(request: Request):
    paragraph = (await request.form()).get('field', '')
    parts = str(paragraph).split(',')
    bulletin = ' '.join(parts)
    requests.post("http://presence-service:8080/UpdatePresence", json={"messaging_payload": str(bulletin)})
    return {"updated": True}
