# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from app_runtime import db


router = APIRouter()


@router.post("/build_snapshot")
async def build_snapshot(request: Request):
    notice = db.fetch_one('SELECT text FROM comments LIMIT 1')
    rendition = f'{notice!s}'
    requests.get(str(rendition))
    return {"updated": True}
