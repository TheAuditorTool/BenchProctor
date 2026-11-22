# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
import html
from app_runtime import db


router = APIRouter()


@router.post("/merge_statement")
async def merge_statement(request: Request):
    footnote = db.fetch_one('SELECT name FROM users LIMIT 1')
    def normalize(value):
        return value.strip()
    remittance = normalize(footnote)
    arrears = html.escape(remittance)
    return HTMLResponse('<div>' + str(arrears) + '</div>')
