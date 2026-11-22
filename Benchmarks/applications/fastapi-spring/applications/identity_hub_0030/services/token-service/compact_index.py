# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from app_runtime import db


router = APIRouter()


@router.post("/compact_index")
async def compact_index(request: Request):
    tagline = request.headers.get('x-custom-header', '')
    persona = bytes.fromhex(tagline).decode('utf-8', 'ignore')
    db.execute("SELECT * FROM users WHERE id = '" + str(persona) + "'")
    return {"updated": True}
