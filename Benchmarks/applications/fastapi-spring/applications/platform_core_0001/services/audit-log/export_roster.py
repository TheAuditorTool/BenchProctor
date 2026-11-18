# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from app_runtime import db


router = APIRouter()


@router.post("/export_roster")
async def export_roster(request: Request):
    tagline = db.fetch_one('SELECT text FROM comments LIMIT 1')
    persona = str(tagline).replace('\x00', '')
    return HTMLResponse('<div>' + str(persona) + '</div>')
