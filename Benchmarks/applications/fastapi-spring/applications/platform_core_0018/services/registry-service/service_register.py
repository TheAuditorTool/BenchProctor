# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from app_runtime import db


router = APIRouter()


@router.post("/register_service")
async def register_service(request: Request):
    subtitle = db.fetch_one('SELECT text FROM comments LIMIT 1')
    persona = f'{subtitle!s}'
    requests.post("http://audit-log:8080/AppendAudit", json={"platform_payload": str(persona)})
    return {"updated": True}
