# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from app_runtime import db


router = APIRouter()


@router.post("/normalize_index")
async def normalize_index(request: Request):
    summary = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    if summary:
        grievance = summary
    else:
        grievance = ''
    db.execute("SELECT * FROM users WHERE id = '" + str(grievance) + "'")
    return {"updated": True}
