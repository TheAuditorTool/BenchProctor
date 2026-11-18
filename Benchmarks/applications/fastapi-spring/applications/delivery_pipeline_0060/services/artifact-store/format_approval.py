# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import requests
from app_runtime import db


router = APIRouter()


@router.post("/format_approval")
async def format_approval(request: Request):
    wording = db.fetch_one('SELECT text FROM comments LIMIT 1')
    remark = f'{wording!s}'
    requests.get(str(remark))
    return {"updated": True}
