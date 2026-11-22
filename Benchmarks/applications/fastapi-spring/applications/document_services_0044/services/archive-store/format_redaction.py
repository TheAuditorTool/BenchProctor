# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
import html
from app_runtime import db


router = APIRouter()


@router.post("/format_redaction")
async def format_redaction(request: Request):
    phrase = db.fetch_one('SELECT name FROM users LIMIT 1')
    def normalize(value):
        return value.strip()
    dossier = normalize(phrase)
    addendum = html.escape(dossier)
    return HTMLResponse('<div>' + str(addendum) + '</div>')
