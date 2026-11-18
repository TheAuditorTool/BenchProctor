# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from app_runtime import db


router = APIRouter()


@router.post("/validate_mapping")
async def validate_mapping(request: Request):
    snippet = (await request.json()).get('payload', '')
    if snippet:
        handshake = snippet
    else:
        handshake = ''
    db.execute("SELECT * FROM users WHERE id = '" + str(handshake) + "'")
    return {"updated": True}
