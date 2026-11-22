# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
import html
from app_runtime import db


router = APIRouter()


@router.post("/enrich_profile")
async def enrich_profile(request: Request):
    notice = db.fetch_one('SELECT name FROM users LIMIT 1')
    def normalize(value):
        return value.strip()
    backorder = normalize(notice)
    voucher = html.escape(backorder)
    return HTMLResponse('<div>' + str(voucher) + '</div>')
