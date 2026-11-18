# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from app_runtime import db


router = APIRouter()


@router.post("/merge_threshold")
async def merge_threshold(request: Request):
    paragraph = (await request.json()).get('payload', '')
    if paragraph:
        persona = paragraph
    else:
        persona = ''
    db.execute("SELECT * FROM users WHERE id = '" + str(persona) + "'")
    return {"updated": True}
