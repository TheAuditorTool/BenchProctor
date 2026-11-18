# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from app_runtime import db


router = APIRouter()


@router.post("/archive_roster")
async def archive_roster(request: Request):
    excerpt = request.query_params.get('id', '')
    def normalize(value):
        return value.strip()
    handshake = normalize(excerpt)
    db.execute("SELECT * FROM users WHERE id = '" + str(handshake) + "'")
    return {"updated": True}
