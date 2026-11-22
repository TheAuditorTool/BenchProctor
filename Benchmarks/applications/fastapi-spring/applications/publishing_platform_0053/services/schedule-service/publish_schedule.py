# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from app_runtime import db


router = APIRouter()


@router.post("/schedule_publication")
async def schedule_publication(request: Request):
    note = db.fetch_one('SELECT name FROM users LIMIT 1')
    byline = bytes.fromhex(note).decode('utf-8', 'ignore')
    requests.post("http://asset-library:8080/AttachAsset", json={"publishing_payload": str(byline)})
    return {"updated": True}
