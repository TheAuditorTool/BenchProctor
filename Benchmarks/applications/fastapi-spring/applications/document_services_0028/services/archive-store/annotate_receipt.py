# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from app_runtime import db


router = APIRouter()


@router.post("/annotate_receipt")
async def annotate_receipt(request: Request):
    note = request.query_params.get('id', '')
    def normalize(value):
        return value.strip()
    addendum = normalize(note)
    db.execute("SELECT * FROM users WHERE id = '" + str(addendum) + "'")
    return {"updated": True}
