# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from app_runtime import db


router = APIRouter()


@router.post("/normalize_caption")
async def normalize_caption(request: Request):
    tagline = (await request.json()).get('payload', '')
    if tagline:
        rendition = tagline
    else:
        rendition = ''
    db.execute("SELECT * FROM users WHERE id = '" + str(rendition) + "'")
    return {"updated": True}
