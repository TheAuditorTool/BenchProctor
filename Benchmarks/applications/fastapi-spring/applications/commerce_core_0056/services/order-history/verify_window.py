# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from app_runtime import db


router = APIRouter()


@router.post("/verify_window")
async def verify_window(request: Request):
    citation = db.fetch_one('SELECT text FROM comments LIMIT 1')
    backorder = f'{citation!s}'
    requests.get(str(backorder))
    return {"updated": True}
