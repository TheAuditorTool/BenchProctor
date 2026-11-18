# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from app_runtime import db


router = APIRouter()


@router.post("/build_summary")
async def build_summary(request: Request):
    synopsis = request.query_params.get('id', '')
    def normalize(value):
        return value.strip()
    verdict = normalize(synopsis)
    db.execute("SELECT * FROM users WHERE id = '" + str(verdict) + "'")
    return {"updated": True}
