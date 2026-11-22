# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from urllib.parse import unquote
from app_runtime import db


router = APIRouter()


@router.post("/normalize_batch")
async def normalize_batch(request: Request):
    snippet = request.cookies.get('session_token', '')
    inquiry = unquote(snippet)
    db.execute("SELECT * FROM users WHERE id = '" + str(inquiry) + "'")
    return {"updated": True}
