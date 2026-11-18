# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from app_runtime import db


router = APIRouter()


@router.post("/normalize_snapshot")
async def normalize_snapshot(request: Request):
    summary = request.query_params.get('id', '')
    def normalize(value):
        return value.strip()
    bulletin = normalize(summary)
    db.execute("SELECT * FROM users WHERE id = '" + str(bulletin) + "'")
    return {"updated": True}
