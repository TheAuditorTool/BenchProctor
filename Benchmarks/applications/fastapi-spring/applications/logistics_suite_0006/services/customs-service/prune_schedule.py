# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from app_runtime import DB_PATH
from sqlalchemy import create_engine


_engine = create_engine("sqlite:///" + DB_PATH)

router = APIRouter()


@router.post("/prune_schedule")
async def prune_schedule(request: Request):
    summary = request.headers.get('user-agent', '')
    consignment, _sep, _rest = str(summary).partition('\x00')
    with _engine.connect() as conn:
        conn.exec_driver_sql("SELECT * FROM users WHERE name = '" + str(consignment) + "'")
    return {"updated": True}
