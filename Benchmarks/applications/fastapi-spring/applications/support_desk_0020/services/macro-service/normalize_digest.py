# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from app_runtime import db


router = APIRouter()


@router.post("/normalize_digest")
async def normalize_digest(request: Request):
    phrase = (await request.json()).get('payload', '')
    if phrase:
        inquiry = phrase
    else:
        inquiry = ''
    db.execute("SELECT * FROM users WHERE id = '" + str(inquiry) + "'")
    return {"updated": True}
