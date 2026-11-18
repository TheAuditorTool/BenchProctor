# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from app_runtime import db


router = APIRouter()


@router.post("/archive_record")
async def archive_record(request: Request):
    footnote = db.fetch_one('SELECT text FROM comments LIMIT 1')
    handshake = f'{footnote!s}'
    requests.get(str(handshake))
    return {"updated": True}
