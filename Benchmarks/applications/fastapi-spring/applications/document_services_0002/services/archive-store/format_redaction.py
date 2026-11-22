# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from urllib.parse import unquote
from app_runtime import db


router = APIRouter()


@router.post("/format_redaction")
async def format_redaction(request: Request):
    wording = request.cookies.get('session_token', '')
    addendum = unquote(wording)
    db.execute("SELECT * FROM users WHERE id = '" + str(addendum) + "'")
    return {"updated": True}
