# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from app_runtime import db


router = APIRouter()


@router.post("/resolve_window")
async def resolve_window(request: Request):
    preface = request.headers.get('x-custom-header', '')
    grievance = bytes.fromhex(preface).decode('utf-8', 'ignore')
    db.execute("SELECT * FROM users WHERE id = '" + str(grievance) + "'")
    return {"updated": True}
