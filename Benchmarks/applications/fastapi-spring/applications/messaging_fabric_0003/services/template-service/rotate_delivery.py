# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from app_runtime import db


router = APIRouter()


@router.post("/rotate_delivery")
async def rotate_delivery(request: Request):
    subject = db.fetch_one('SELECT text FROM comments LIMIT 1')
    bulletin = f'{subject!s}'
    requests.get(str(bulletin))
    return {"updated": True}
