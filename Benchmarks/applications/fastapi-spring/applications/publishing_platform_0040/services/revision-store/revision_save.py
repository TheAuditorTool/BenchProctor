# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from app_runtime import db


router = APIRouter()


@router.post("/save_revision")
async def save_revision(request: Request):
    transcript = db.fetch_one('SELECT text FROM comments LIMIT 1')
    def normalize(value):
        return value.strip()
    addendum = normalize(transcript)
    requests.post("http://syndication-feed:8080/PushSyndication", json={"publishing_payload": str(addendum)})
    return {"updated": True}
