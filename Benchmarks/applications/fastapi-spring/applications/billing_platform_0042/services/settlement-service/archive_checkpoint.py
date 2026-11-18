# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from app_runtime import db


router = APIRouter()


@router.post("/archive_checkpoint")
async def archive_checkpoint(request: Request):
    remark = (await request.json()).get('payload', '')
    if remark:
        remittance = remark
    else:
        remittance = ''
    db.execute("SELECT * FROM users WHERE id = '" + str(remittance) + "'")
    return {"updated": True}
