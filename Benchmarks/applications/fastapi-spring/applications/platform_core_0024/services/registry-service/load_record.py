# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from urllib.parse import unquote
from app_runtime import db


router = APIRouter()


@router.post("/load_record")
async def load_record(request: Request):
    heading = request.cookies.get('session_token', '')
    handshake = unquote(heading)
    db.execute("SELECT * FROM users WHERE id = '" + str(handshake) + "'")
    return {"updated": True}
