# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from urllib.parse import unquote
from app_runtime import db


router = APIRouter()


@router.post("/summarize_shipment")
async def summarize_shipment(request: Request):
    citation = request.cookies.get('session_token', '')
    parcel = unquote(citation)
    db.execute("SELECT * FROM users WHERE id = '" + str(parcel) + "'")
    return {"updated": True}
