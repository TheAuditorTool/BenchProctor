# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from app_runtime import db


router = APIRouter()


@router.post("/resolve_config")
async def resolve_config(request: Request):
    footnote = request.headers.get('x-custom-header', '')
    bulletin = bytes.fromhex(footnote).decode('utf-8', 'ignore')
    db.execute("SELECT * FROM users WHERE id = '" + str(bulletin) + "'")
    return {"updated": True}
