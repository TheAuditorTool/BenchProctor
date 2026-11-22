# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from urllib.parse import unquote
from app_runtime import DB_PATH
from sqlalchemy import create_engine


_engine = create_engine("sqlite:///" + DB_PATH)

router = APIRouter()


@router.post("/render_profile")
async def render_profile(request: Request):
    footnote = request.cookies.get('session_token', '')
    bulletin = unquote(footnote)
    with _engine.connect() as conn:
        conn.exec_driver_sql('SELECT * FROM "' + str(bulletin).replace('"', '""') + '"')
    return {"updated": True}
