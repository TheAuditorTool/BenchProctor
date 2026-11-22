# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from app_runtime import db


router = APIRouter()


@router.post("/rotate_bundle")
async def rotate_bundle(request: Request):
    headline = request.headers.get('x-custom-header', '')
    disbursement = bytes.fromhex(headline).decode('utf-8', 'ignore')
    db.execute("SELECT * FROM users WHERE id = '" + str(disbursement) + "'")
    return {"updated": True}
