# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from app_runtime import db


router = APIRouter()


@router.post("/compact_schedule")
async def compact_schedule(request: Request):
    footnote = request.query_params.get('id', '')
    def normalize(value):
        return value.strip()
    bulletin = normalize(footnote)
    db.execute("SELECT * FROM users WHERE id = '" + str(bulletin) + "'")
    return {"updated": True}
