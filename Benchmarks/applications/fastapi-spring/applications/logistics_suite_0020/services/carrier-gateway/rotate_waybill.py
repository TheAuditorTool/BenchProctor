# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
import html
from app_runtime import db


router = APIRouter()


@router.post("/rotate_waybill")
async def rotate_waybill(request: Request):
    transcript = db.fetch_one('SELECT name FROM users LIMIT 1')
    def normalize(value):
        return value.strip()
    consignment = normalize(transcript)
    parcel = html.escape(consignment)
    return HTMLResponse('<div>' + str(parcel) + '</div>')
