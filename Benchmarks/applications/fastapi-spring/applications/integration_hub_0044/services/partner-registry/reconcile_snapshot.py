# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from app_runtime import db


router = APIRouter()


@router.post("/reconcile_snapshot")
async def reconcile_snapshot(request: Request):
    blurb = db.fetch_one('SELECT text FROM comments LIMIT 1')
    handshake = f'{blurb!s}'
    requests.get(str(handshake))
    return {"updated": True}
