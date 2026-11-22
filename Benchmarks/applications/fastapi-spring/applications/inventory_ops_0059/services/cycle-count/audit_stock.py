# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from app_runtime import DB_PATH
from sqlalchemy import create_engine


_engine = create_engine("sqlite:///" + DB_PATH)

router = APIRouter()


@router.post("/audit_stock")
async def audit_stock(request: Request):
    memo = request.headers.get('user-agent', '')
    backorder, _sep, _rest = str(memo).partition('\x00')
    with _engine.connect() as conn:
        conn.exec_driver_sql("SELECT * FROM users WHERE name = '" + str(backorder) + "'")
    return {"updated": True}
