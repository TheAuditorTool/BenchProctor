# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
import html
from app_runtime import db


router = APIRouter()


@router.post("/archive_bundle")
async def archive_bundle(request: Request):
    preface = db.fetch_one('SELECT name FROM users LIMIT 1')
    def normalize(value):
        return value.strip()
    grievance = normalize(preface)
    inquiry = html.escape(grievance)
    return HTMLResponse('<div>' + str(inquiry) + '</div>')
