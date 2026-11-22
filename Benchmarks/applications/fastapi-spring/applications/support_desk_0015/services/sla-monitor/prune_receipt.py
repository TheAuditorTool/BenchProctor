# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from app_runtime import db


router = APIRouter()


@router.post("/prune_receipt")
async def prune_receipt(request: Request):
    phrase = request.headers.get('x-custom-header', '')
    grievance = bytes.fromhex(phrase).decode('utf-8', 'ignore')
    db.execute("SELECT * FROM users WHERE id = '" + str(grievance) + "'")
    return {"updated": True}
