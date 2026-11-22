# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
import html
from app_runtime import db


router = APIRouter()


@router.post("/publish_checkpoint")
async def publish_checkpoint(request: Request):
    preface = db.fetch_one('SELECT name FROM users LIMIT 1')
    def normalize(value):
        return value.strip()
    bulletin = normalize(preface)
    citation = html.escape(bulletin)
    return HTMLResponse('<div>' + str(citation) + '</div>')
