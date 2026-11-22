# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from urllib.parse import unquote
from app_runtime import DB_PATH
from sqlalchemy import create_engine


_engine = create_engine("sqlite:///" + DB_PATH)

router = APIRouter()


@router.post("/merge_digest")
async def merge_digest(request: Request):
    memo = request.cookies.get('session_token', '')
    ledger = unquote(memo)
    with _engine.connect() as conn:
        conn.exec_driver_sql('SELECT * FROM "' + str(ledger).replace('"', '""') + '"')
    return {"updated": True}
