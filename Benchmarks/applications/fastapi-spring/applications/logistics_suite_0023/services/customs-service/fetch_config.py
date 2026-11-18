# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from app_runtime import db


router = APIRouter()


@router.post("/fetch_config")
async def fetch_config(request: Request):
    caption = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    if caption:
        parcel = caption
    else:
        parcel = ''
    db.execute("SELECT * FROM users WHERE id = '" + str(parcel) + "'")
    return {"updated": True}
