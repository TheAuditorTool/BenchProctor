# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from app_runtime import db


router = APIRouter()


@router.post("/fetch_report")
async def fetch_report(request: Request):
    paragraph = request.headers.get('x-custom-header', '')
    gauge = bytes.fromhex(paragraph).decode('utf-8', 'ignore')
    db.execute("SELECT * FROM users WHERE id = '" + str(gauge) + "'")
    return {"updated": True}
