# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from app_runtime import db


router = APIRouter()


@router.post("/load_window")
async def load_window(request: Request):
    heading = (await request.json()).get('payload', '')
    if heading:
        voucher = heading
    else:
        voucher = ''
    db.execute("SELECT * FROM users WHERE id = '" + str(voucher) + "'")
    return {"updated": True}
