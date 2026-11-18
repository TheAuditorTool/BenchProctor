# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from app_runtime import db


router = APIRouter()


@router.post("/export_digest")
async def export_digest(request: Request):
    blurb = request.query_params.get('id', '')
    def normalize(value):
        return value.strip()
    handshake = normalize(blurb)
    db.execute("SELECT * FROM users WHERE id = '" + str(handshake) + "'")
    return {"updated": True}
