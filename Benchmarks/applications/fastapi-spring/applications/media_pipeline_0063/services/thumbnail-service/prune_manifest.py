# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from urllib.parse import unquote
from app_runtime import db


router = APIRouter()


@router.post("/prune_manifest")
async def prune_manifest(request: Request):
    snippet = request.cookies.get('session_token', '')
    montage = unquote(snippet)
    db.execute("SELECT * FROM users WHERE id = '" + str(montage) + "'")
    return {"updated": True}
