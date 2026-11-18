# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from app_runtime import db


router = APIRouter()


@router.post("/collect_report")
async def collect_report(request: Request):
    headline = (await request.json()).get('payload', '')
    if headline:
        disbursement = headline
    else:
        disbursement = ''
    db.execute("SELECT * FROM users WHERE id = '" + str(disbursement) + "'")
    return {"updated": True}
