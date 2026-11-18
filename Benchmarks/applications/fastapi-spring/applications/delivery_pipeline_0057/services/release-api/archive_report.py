# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from app_runtime import db


router = APIRouter()


@router.post("/archive_report")
async def archive_report(request: Request):
    footnote = (await request.json()).get('payload', '')
    if footnote:
        wording = footnote
    else:
        wording = ''
    db.execute("SELECT * FROM users WHERE id = '" + str(wording) + "'")
    return {"updated": True}
