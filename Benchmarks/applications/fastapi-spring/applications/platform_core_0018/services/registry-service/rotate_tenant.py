# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from urllib.parse import unquote
from app_runtime import DB_PATH
from sqlalchemy import create_engine


_engine = create_engine("sqlite:///" + DB_PATH)

router = APIRouter()


@router.post("/rotate_tenant")
async def rotate_tenant(request: Request):
    subtitle = request.cookies.get('session_token', '')
    persona = unquote(subtitle)
    with _engine.connect() as conn:
        conn.exec_driver_sql('SELECT * FROM "' + str(persona).replace('"', '""') + '"')
    return {"updated": True}
