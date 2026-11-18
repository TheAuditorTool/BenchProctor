# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from app_runtime import db


router = APIRouter()


@router.post("/resolve_header")
async def resolve_header(request: Request):
    summary = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    if summary:
        cohort = summary
    else:
        cohort = ''
    db.execute("SELECT * FROM users WHERE id = '" + str(cohort) + "'")
    return {"updated": True}
