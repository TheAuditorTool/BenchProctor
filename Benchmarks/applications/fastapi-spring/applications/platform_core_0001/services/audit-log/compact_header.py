# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from app_runtime import db


router = APIRouter()


@router.post("/compact_header")
async def compact_header(request: Request):
    tagline = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    if tagline:
        persona = tagline
    else:
        persona = ''
    db.execute("SELECT * FROM users WHERE id = '" + str(persona) + "'")
    return {"updated": True}
