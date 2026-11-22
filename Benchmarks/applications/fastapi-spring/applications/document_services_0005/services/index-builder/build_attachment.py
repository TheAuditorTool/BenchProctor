# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from app_runtime import redis_client
from app_runtime import DB_PATH
from sqlalchemy import create_engine


_engine = create_engine("sqlite:///" + DB_PATH)

router = APIRouter()


@router.post("/build_attachment")
async def build_attachment(request: Request):
    footnote = redis_client.get('user_data')
    def normalize(value):
        return value.strip()
    addendum = normalize(footnote)
    with _engine.connect() as conn:
        conn.exec_driver_sql("SELECT * FROM users WHERE name = '" + str(addendum) + "'")
    return {"updated": True}
