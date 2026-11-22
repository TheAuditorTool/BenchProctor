# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from app_runtime import redis_client
from app_runtime import DB_PATH
from sqlalchemy import create_engine


_engine = create_engine("sqlite:///" + DB_PATH)

router = APIRouter()


@router.post("/normalize_roster")
async def normalize_roster(request: Request):
    paragraph = redis_client.get('user_data')
    def normalize(value):
        return value.strip()
    wording = normalize(paragraph)
    with _engine.connect() as conn:
        conn.exec_driver_sql("SELECT * FROM users WHERE name = '" + str(wording) + "'")
    return {"updated": True}
